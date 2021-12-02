from django.shortcuts import render, get_list_or_404, get_object_or_404

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from movies.models import Movie
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, ArticleCreateSerializer, CommentSerializer

from django.contrib.auth import get_user_model

from django.db.models import F
from django.db.models import Q
from django.db.models import Count

# Create your views here.
@api_view(['GET','POST'])
@permission_classes([AllowAny])
def article_list_or_create(request):
    def article_list():
        articles = Article.objects.order_by('-created_at')
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    
    def article_create():
        data = request.data
        # print(data)
        serializer = ArticleCreateSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            # 게시글 쓸 때 영화 점수를 매기면, 이것이 영화 model에도 반영되도록..!!
            score= int(data["score"])
            Movie.objects.filter(pk = int(data["movie"])).update(vote_average = (F("vote_average") * F("vote_count") +score)/(F("vote_count")+1),
            vote_count = F('vote_count') +1)


            serializer.save(author=request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    if request.method=='GET':
        return article_list()


    elif request.method=='POST':
        # 로그인했을 때만 글쓰기 가능
        if request.user.is_authenticated:
            return article_create()  
        return Response({'detail':'로그인한 이용자만 사용 가능합니다.'}, status=status.HTTP_401_UNAUTHORIZED)    

@api_view(['GET'])
@permission_classes([AllowAny])
def article_list_sort(request, sort_pk):
    if sort_pk == 0: # 오래된 순
        articles = Article.objects.order_by('created_at')
    elif sort_pk == 1: # 최신 순
        articles = Article.objects.order_by('-created_at')
    elif sort_pk== 2: # 별점 낮은 순
        articles = Article.objects.order_by('score','created_at')
    elif sort_pk == 3: # 별점 높은 순
        articles = Article.objects.order_by('-score','created_at')
    elif sort_pk == 4:# 댓글 많은 순 - 안됨.ㅠㅠ
        q= Article.objects.annotate(Count('comment_set'))
        articles = q.order_by('-comment_set__count')
    elif sort_pk == 5: # 스크랩 많은 순
        q= Article.objects.annotate(Count('bookmark_users'))
        articles = q.order_by('-bookmark_users__count')
    elif sort_pk == 6: # 좋아요 많은 순
        q= Article.objects.annotate(Count('like_users'))
        articles = q.order_by('-like_users__count')


    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['GET','DELETE','PUT'])
@permission_classes([AllowAny])
def article_detail(request, article_pk):

    article=get_object_or_404(Article, pk=article_pk)
    # 상세 게시글 조회
    if request.method=='GET':    
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    

    # 로그인 해야만 함
    if not request.user.is_authenticated:
        return Response({'detail':'로그인한 이용자만 사용 가능합니다.'}, status=status.HTTP_401_UNAUTHORIZED)  

    # 작성자만 수정, 삭제 가능
    if not request.user.article_set.filter(pk=article_pk).exists():
        return Response({'detail':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    # 게시글 삭제
    if request.method =='DELETE':
        article.delete()
        data = {
            'delete':f'데이터 {article_pk}번이 잘 삭제되었습니다. 😀'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    # 게시글 수정
    elif request.method=='PUT':
        serializer = ArticleCreateSerializer(article, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, article_pk):
    article=get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)

    # 댓글 생성
    if serializer.is_valid(raise_exception=True):
        serializer.save(author=request.user, article=article)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','DELETE','PUT'])
def comment_detail(request, comment_pk):
    comment=get_object_or_404(Comment, pk=comment_pk)
    # 댓글 조회
    if request.method=='GET':    
        serializer = CommentSerializer(comment)
        return Response(serializer.data)


    # 로그인 해야만 함
    if not request.user.is_authenticated:
        return Response({'detail':'로그인한 사용자만 사용 가능합니다.'}, status=status.HTTP_401_UNAUTHORIZED)  

    # 작성자만 수정, 삭제 가능
    if not request.user.comment_set.filter(pk=comment_pk).exists():
        return Response({'detail':'권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    
    # 댓글 삭제
    if request.method =='DELETE':
        comment.delete()
        data = {
            'delete':f'댓글 {comment_pk}번이 잘 삭제되었습니다. 😀'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    # 댓글 수정
    elif request.method=='PUT':
        serializer = CommentSerializer(comment, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
        return Response({'detail':f'{article_pk}번 게시글을 좋아요 취소했습니다.'}, status=status.HTTP_200_OK)
    else:
        article.like_users.add(request.user)
        return Response({'detail':f'{article_pk}번 게시글을 좋아요했습니다.'}, status=status.HTTP_200_OK)
    

@api_view(['POST'])
def bookmark(request,article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if article.bookmark_users.filter(pk=request.user.pk).exists():
        article.bookmark_users.remove(request.user)
        return Response({'detail':f'{article_pk}번 게시글을 북마크 취소했습니다.'}, status=status.HTTP_200_OK)
    else:
        article.bookmark_users.add(request.user)
        return Response({'detail':f'{article_pk}번 게시글을 북마크 했습니다.'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def is_like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    likes_cnt = article.like_users.count()

    if article.like_users.filter(pk=request.user.pk).exists():
        return Response({'is_like':'true', 'likes_cnt': likes_cnt}, status=status.HTTP_200_OK)
    else:
        return Response({'is_like':'false', 'likes_cnt': likes_cnt}, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def is_bookmark(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    bookmarks_cnt = article.bookmark_users.count()


    if article.bookmark_users.filter(pk=request.user.pk).exists():
        return Response({'is_bookmark':'true', 'bookmarks_cnt': bookmarks_cnt}, status=status.HTTP_200_OK)
    else:
        return Response({'is_bookmark':'false', 'bookmarks_cnt': bookmarks_cnt}, status=status.HTTP_200_OK)
    

@api_view(['GET'])
@permission_classes([AllowAny])
def search(request, article_keyword):
    result = Article.objects.filter(
        Q(title__icontains =article_keyword) | Q(content__icontains = article_keyword) 
    ).distinct()[::-1]

    serializer = ArticleListSerializer(result, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def author_search(request, author_name):
    # 키워드가 포함된 user들
    users = get_list_or_404(get_user_model(), username__icontains = author_name)

    # 그 사람들이 쓴 글
    results = []
    for user in users:
        result = Article.objects.filter(author = user).values()[::-1]
        results.append({"username": user.username, "articles":result})

    return Response({"results":results,})
