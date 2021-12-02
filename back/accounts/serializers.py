from rest_framework import serializers
from django.contrib.auth import get_user_model
from articles.models import Article, Comment
from movies.models import Movie

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username','password','mbti')



class UserProfileSerializer(serializers.ModelSerializer):

    class ArticleSerializer(serializers.ModelSerializer):
    
        class MovieSerializer(serializers.ModelSerializer):
            class Meta:
                model = Movie
                fields = ('title','id')

        movie = MovieSerializer()

        class Meta:
            model = Article
            fields = ('pk','title', 'movie')
    
    article_set = ArticleSerializer(many=True)
    article_count = serializers.IntegerField(source="article_set.count", read_only=True)

    bookmarked_articles = ArticleSerializer(many=True)
    bookmarked_articles_count = serializers.IntegerField(source="bookmarked_articles.count", read_only=True)

    class CommentSerializer(serializers.ModelSerializer):

        class ArticleSerializer(serializers.ModelSerializer):
            class Meta:
                model = Article
                fields=('title','id') 
        
        article= ArticleSerializer()

        class Meta:
            model = Comment
            fields =('pk','article','content')
    
    comment_set = CommentSerializer(many=True)
    comment_count = serializers.IntegerField(source="comment_set.count", read_only = True)


    following_cnt = serializers.IntegerField(
        source='followings.count',
        read_only=True
    )

    

    follower_cnt = serializers.IntegerField(
        source='followers.count',
        read_only=True
    )

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields =('pk','title',)
    
    picked_movies = MovieSerializer(many=True)
    picked_movies_count = serializers.IntegerField(source="picked_movies.count", read_only=True)
    

    class Meta:
        model = get_user_model()
        fields=('id','username','mbti', 'poster_number','article_set','article_count','comment_set','comment_count','following_cnt','follower_cnt','picked_movies','picked_movies_count','bookmarked_articles','bookmarked_articles_count')