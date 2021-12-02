from django.shortcuts import render, get_list_or_404, get_object_or_404

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import Movie, Genre
from .serializers import MovieListSerializer, MovieSerializer, RecommendMovieSerializer

from django.contrib.auth import get_user_model
from django.db.models import Q
from django.db.models import Count

import random
import requests
import json

from django.conf import settings

# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list_sort(request, sort_pk):
    if sort_pk == 0: # 점수 높은 순
        movies = Movie.objects.order_by('-vote_average')
    elif sort_pk == 1: # 점수 낮은 순
        movies = Movie.objects.order_by('vote_average')
    elif sort_pk == 2: # 최신 
        movies = Movie.objects.order_by('-release_date')
    elif sort_pk == 3: # 오래된 순 
        movies = Movie.objects.order_by('release_date')
    elif sort_pk == 4: # 찜한 유저가 많은 순 
        q = Movie.objects.annotate(Count('pick_users'))
        movies = q.order_by('pick_users__count')
    
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def pick(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if movie.pick_users.filter(pk=request.user.pk).exists():
        movie.pick_users.remove(request.user)
        return Response({'detail':f'{movie_pk}번 영화를 찜 취소했습니다.'}, status=status.HTTP_200_OK)
    else:
        movie.pick_users.add(request.user)
        return Response({'detail':f'{movie_pk}번 영화를 찜했습니다.'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def is_pick(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    picks_cnt = movie.pick_users.count()

    if movie.pick_users.filter(pk=request.user.pk).exists():
        return Response({'is_pick':'true','picks_cnt':picks_cnt}, status=status.HTTP_200_OK)
    else:
        return Response({'is_pick':'false','picks_cnt':picks_cnt}, status=status.HTTP_200_OK)



@api_view(['GET'])
@permission_classes([AllowAny])
def mbti_recommend(request, mbti_name):

    if mbti_name == "null":
        # null이 들어왔을 때
        return Response({"detail" :"null이 들어오면 안됩니다."}, status=status.HTTP_404_NOT_FOUND)

    else:
        mbti_movie_recommendation = {
                'istj' : [36, 10770, 10752],
                'isfj' : [10402, 99, 36],
                'infj' : [18, 10751, 10770],
                'intj' : [9648, 53, 878],
                'istp' : [80, 35, 36],
                'isfp' : [16, 14, 12],
                'infp' : [14],
                'intp' : [878,9648],
                'estp' : [28, 80],
                'esfp' : [12,10752],
                'enfp' : [12,28],
                'entp' : [35,80,99],
                'estj' : [18,99,12],
                'esfj' : [10749,10402],
                'enfj' : [10749,10402,18],
                'entj' : [27, 53, 80],
            }
        recommendation_movies = set()
        recommendation_genres = mbti_movie_recommendation[mbti_name.lower()]

        for recommendation_genre in recommendation_genres:
            genre = get_object_or_404(Genre, pk=recommendation_genre)
            movies = genre.movie_set.all()
            recommendation_movies.update(movies)

        recommendation_movies_pick = random.sample(list(recommendation_movies),10)
        serializer = MovieListSerializer(recommendation_movies_pick, many=True)
        return Response(serializer.data)
    
    


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_recommend(request, movie_pk):       
    movie = get_object_or_404(Movie, pk=movie_pk) 
    # TMDB API로 추천 영화 받아오기    
    api_key = settings.TMDB_API_KEY
    url = f"https://api.themoviedb.org/3/movie/{movie_pk}/recommendations?api_key={api_key}&language=en-US&page=1"
    recommend_movies = requests.get(url).json().get('results')
    if recommend_movies:
        results = []

        for recommend_movie in recommend_movies:
            
            tmp = {
                'title' :'',
                'poster_path':'',
                'id':'',
            }

            tmp['title']=recommend_movie['title']
            tmp['poster_path'] = recommend_movie['poster_path']
            tmp['id'] = recommend_movie['id']
            results.append(tmp)
        
        serializer = RecommendMovieSerializer(results, many=True)

        return Response(serializer.data)

    return Response({'detail':f'{movie_pk}번 영화의 추천 영화가 없습니다.'}, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
@permission_classes([AllowAny])
def reviews(request, movie_pk):

    movie = get_object_or_404(Movie, pk= movie_pk)
    results = []

    # 우리 review 받아오기
    our_reviews = movie.articles.values()
    our_reviews_count = len(our_reviews)
    for i in range(our_reviews_count):
        our_review =our_reviews[i]
        print(our_review)
        author = get_object_or_404(get_user_model(), pk = our_review["author_id"])
        
        tmp = author.poster_number
        if tmp == 0:
            tmp = 1

        # avatar_path = "../assets/profile_img"+str(tmp)+".gif"
        avatar_path = tmp

        tmp = {
                "id":"",
                "author":"",
                "content":"",
                "avatar_path": avatar_path,
                "rating":"",
            }
        tmp["id"] = i
        tmp["author"]= author.username
        tmp["content"]=our_review['content']
        tmp["rating"]=our_review['score']
        
        results.append(tmp)



    # TMDB의 review 받아오기

    api_key = settings.TMDB_API_KEY
    tmdb_pk = movie.tmdb_pk
    url = f"https://api.themoviedb.org/3/movie/{tmdb_pk}/reviews?api_key={api_key}&language=en-US&page=1"
    reviews = requests.get(url).json().get('results')
    if reviews:
    
        for i in range(len(reviews)):
            review = reviews[i]
            # 11/22 kaye - id, avatar_path, rating 추가, response 오타 수정
            
            tmp = {
                "id":"",
                "author":"",
                "content":"",
                "avatar_path":"",
                "rating":"",
            }
            
            tmp["id"]= i + our_reviews_count
            tmp["author"]=review["author"]
            tmp["content"]=review["content"]
            tmp["avatar_path"]="https://image.tmdb.org/t/p/w500"+review["author_details"]["avatar_path"]
            tmp["rating"]=review["author_details"]["rating"]
            
            results.append(tmp)

    # 리뷰가 하나 이상이면
    if results:
        return Response({'reviews':results})

    # 리뷰가 전혀 없으면
    return Response({'detail':f'{movie_pk}번 영화의 리뷰가 없습니다.'}, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
@permission_classes([AllowAny])
def search(request, movie_keyword):
    result = Movie.objects.filter(
        Q(title__icontains =movie_keyword) | Q(overview__icontains = movie_keyword) 
    ).distinct()

    serializer = MovieListSerializer(result, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def actors(request, movie_pk):
    # TMDB에서 그 영화에 나온 배우 정보 가져오기
    api_key = settings.TMDB_API_KEY
    movie = get_object_or_404(Movie, pk= movie_pk)
    tmdb_pk = movie.tmdb_pk
    url = f"https://api.themoviedb.org/3/movie/{tmdb_pk}/credits?api_key={api_key}&language=en-US&page=1"
    credits = requests.get(url).json().get('cast')
    if credits:
        results = []

        for credit in credits:
            
            tmp = {
                "id":"",
                "name":"",
                "profile_path" :"",
                "character" :"",
            }

            tmp["id"]=credit["id"]
            tmp["name"]=credit["name"]
            tmp["profile_path"]=credit["profile_path"]
            tmp["character"]=credit["character"]
            
            results.append(tmp)
        
        return Response({'credits':results})

    return Response({'detail':f'{movie_pk}번 영화의 credit 정보가 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

import datetime
@api_view(['GET'])
@permission_classes([AllowAny])
def today_recommend(request):
    # 날씨 API 이용해서 날씨 받아오기 
    api_key = settings.WEATHER_API_KEY

    now = datetime.datetime.now() - datetime.timedelta(hours=1)
    nowDate = now.strftime('%Y%m%d')

    hour = now.strftime('%H')

    url = f'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey={api_key}&pageNo=1&numOfRows=1000&dataType=JSON&base_date={nowDate}&base_time={hour}00&nx=55&ny=127'

    response = requests.get(url).json()['response']['body']['items']['item']

    # 날씨 추출
    now_weathers = [] # 지금 날씨 관련 특징적인 정보들 저장
    for item in response:

        tmp = item.get("category")
        tmp_val = item.get("obsrValue")

        if tmp == "PTY": # 강수 형태(없음(0), 비(1), 비/눈(2), 눈(3), 빗방울(5), 빗방울눈날림(6), 눈날림(7) )
            if tmp_val == 1 or tmp_val == 5 or tmp_val == 2 or tmp_val == 6:
                now_weathers.append['rain']
            
            elif tmp_val == 3 or tmp_val == 7:
                now_weathers.append('snowy')
            
            else:
                now_weathers.append('sunny')

        elif tmp == "RN1": # 강수량
            pass

        elif tmp =="REH": # 습도
            pass

        elif tmp == "T1H": # 기온
            temperature = float(tmp_val)

            if temperature <= 13: # 겨울(추울 때)
                now_weathers.append('cold')

            elif temperature  <= 21: # 봄, 가을
                now_weathers.append('warm')

            else: # 여름(더울 때)
                now_weathers.append('hot')

        elif tmp == "WSD": # 풍속
            pass

    # 어떤 날씨에 어떤 영화 장르 추천?
    weather_movie_recommendation = {
        'rain': [9648, 53, 80, 27],
        'snowy':[18, 10749, 10751],
        'sunny':[12, 14, 28],
        'cold':[18, 10751],
        'warm':[12, 14, 16],
        'hot':[9648, 53, 80, 27],
    }

    recommendation_genres = set()
    # serializers = {}
    serializers = []
    for now_weather in now_weathers:
        recommendation_genres.update(weather_movie_recommendation[now_weather])

        recommendation_movies = set()
        for recommendation_genre in recommendation_genres:
            genre = get_object_or_404(Genre, pk=recommendation_genre)
            movies = genre.movie_set.all()
            recommendation_movies.update(movies)
    
        serializer = MovieListSerializer(random.sample(recommendation_movies, 10), many = True)

        if now_weather == 'rain':
            now_weather_id = 0
        elif now_weather == 'snowy':
            now_weather_id = 1
        elif now_weather == 'sunny':
            now_weather_id = 2
        elif now_weather == 'cold':
            now_weather_id = 3
        elif now_weather == 'warm':
            now_weather_id = 4
        elif now_weather == 'hot':
            now_weather_id = 5

        # serializers[now_weather] = {"id": now_weather_id, "weather": now_weather,"data":serializer.data}
        serializers.append({"id": now_weather_id, "weather": now_weather,"data":serializer.data})
    
    return Response(serializers)


@api_view(['GET'])
@permission_classes([AllowAny])
def today_recommend_by(request,area):
        # 날씨 API 이용해서 날씨 받아오기 
    api_key = settings.WEATHER_API_KEY

    now = datetime.datetime.now() - datetime.timedelta(hours=1)
    nowDate = now.strftime('%Y%m%d')

    hour = now.strftime('%H')
    
    # 지역별로 구분
    if area == 0 : #서울
        nx, ny = 60, 127
    elif area == 1: # 부산
        nx, ny = 98, 76
    elif area == 2: # 구미
        nx, ny = 84, 96
    elif area == 3: # 광주
        nx, ny = 58, 74
    elif area == 4:  #대전
        nx, ny = 67, 100

    url = f'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey={api_key}&pageNo=1&numOfRows=1000&dataType=JSON&base_date={nowDate}&base_time={hour}00&nx={nx}&ny={ny}'

    response = requests.get(url).json()['response']['body']['items']['item']

    # 날씨 추출
    now_weathers = [] # 지금 날씨 관련 특징적인 정보들 저장
    for item in response:

        tmp = item.get("category")
        tmp_val = item.get("obsrValue")

        if tmp == "PTY": # 강수 형태(없음(0), 비(1), 비/눈(2), 눈(3), 빗방울(5), 빗방울눈날림(6), 눈날림(7) )
            if tmp_val == 1 or tmp_val == 5 or tmp_val == 2 or tmp_val == 6:
                now_weathers.append['rain']
            
            elif tmp_val == 3 or tmp_val == 7:
                now_weathers.append('snowy')
            
            else:
                now_weathers.append('sunny')

        elif tmp == "RN1": # 강수량
            pass

        elif tmp =="REH": # 습도
            pass

        elif tmp == "T1H": # 기온
            temperature = float(tmp_val)

            if temperature <= 13: # 겨울(추울 때)
                now_weathers.append('cold')

            elif temperature  <= 21: # 봄, 가을
                now_weathers.append('warm')

            else: # 여름(더울 때)
                now_weathers.append('hot')

        elif tmp == "WSD": # 풍속
            pass

    # 어떤 날씨에 어떤 영화 장르 추천?
    weather_movie_recommendation = {
        'rain': [9648, 53, 80, 27],
        'snowy':[18, 10749, 10751],
        'sunny':[12, 14, 28],
        'cold':[18, 10751],
        'warm':[12, 14, 16],
        'hot':[9648, 53, 80, 27],
    }

    recommendation_genres = set()
    # serializers = {}
    serializers = []
    for now_weather in now_weathers:
        recommendation_genres.update(weather_movie_recommendation[now_weather])

        recommendation_movies = set()
        for recommendation_genre in recommendation_genres:
            genre = get_object_or_404(Genre, pk=recommendation_genre)
            movies = genre.movie_set.all()
            recommendation_movies.update(movies)
    
        serializer = MovieListSerializer(random.sample(recommendation_movies, 10), many = True)

        if now_weather == 'rain':
            now_weather_id = 0
        elif now_weather == 'snowy':
            now_weather_id = 1
        elif now_weather == 'sunny':
            now_weather_id = 2
        elif now_weather == 'cold':
            now_weather_id = 3
        elif now_weather == 'warm':
            now_weather_id = 4
        elif now_weather == 'hot':
            now_weather_id = 5

        # serializers[now_weather] = {"id": now_weather_id, "weather": now_weather,"data":serializer.data}
        serializers.append({"id": now_weather_id, "weather": now_weather,"data":serializer.data})
    
    return Response(serializers)