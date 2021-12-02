from rest_framework import serializers
from .models import Genre, Movie
from articles.models import Article

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields=('id','title','poster_path',)

class MovieSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name','id')
    
    genres = GenreSerializer(many= True)

    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('author','title','content','created_at','updated_at','score',)


    articles = ArticleSerializer(many=True)

    class Meta:
        model=Movie
        fields=('id','genres','articles','title','overview','release_date','poster_path','vote_count','vote_average','tmdb_pk','actors','pick_users')



class RecommendMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields=('title','poster_path','id')