from rest_framework import serializers
from .models import Article, Comment
from movies.models import Movie

from django.contrib.auth import get_user_model



class ArticleListSerializer(serializers.ModelSerializer):
    
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title','id')

    movie = MovieSerializer()

    class AuthorSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('username','id','poster_number')
    author = AuthorSerializer()

    comment_count = serializers.IntegerField(source="comment_set.count", read_only = True)

    class Meta:
        model = Article
        fields = ('id','title','movie','created_at','score','author','comment_count')


class ArticleSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title','id','poster_path')
            read_only_fields = ('title','poster_path',)

    movie = MovieSerializer()

    class AuthorSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('username','id','poster_number')
    author = AuthorSerializer(read_only = True)

    class CommentSerializer(serializers.ModelSerializer):

        class AuthorSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('username','poster_number')
        author = AuthorSerializer()

        class Meta:
            model = Comment
            fields = ('id', 'author', 'content','created_at','updated_at')
        
    comment_set = CommentSerializer(many=True, read_only = True)

    comment_count = serializers.IntegerField(source="comment_set.count", read_only = True)

    like_users_count = serializers.IntegerField(source="like_users.count", read_only=True)
    bookmark_users_count = serializers.IntegerField(source="bookmark_users.count", read_only=True)

    class Meta:
        model = Article
        fields='__all__'
        read_only_fields=('like_users','bookmark_users',)
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['comment_set'] = sorted(response["comment_set"], key=lambda x:-x["id"])
        return response


class ArticleCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields='__all__'
        read_only_fields=('author', 'like_users','bookmark_users',)



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields='__all__'
        read_only_fields=('author', 'article', )

