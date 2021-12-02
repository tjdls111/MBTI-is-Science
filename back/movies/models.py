from django.db import models
from django.conf import settings

# Create your models here.

class Actor(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Movie(models.Model):
    actors = models.ManyToManyField(Actor, related_name='movies', blank=True)
    pick_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='picked_movies', blank=True)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField(null=True)
    poster_path = models.TextField(null=True)
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    genres = models.ManyToManyField(Genre)
    tmdb_pk = models.IntegerField()

    def __str__(self):
        return f'{self.title}'
