import requests
from pprint import pprint
import json 
from django.conf import settings

# api_key = settings.api_key

my_db_data= []

# 장르 
url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US'
genres = requests.get(url).json()['genres']

for genre in genres:
    my_genre_model = {
        "model":"movies.genre",
        "pk":"",
        "fields":{
            "name":"",
        }
    }

    my_genre_model["pk"] = genre["id"]
    my_genre_model["fields"]["name"] = genre["name"]

    my_db_data.append(my_genre_model)



# 영화
for i in range(1,101):
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page={i}'

    movies = requests.get(url).json()['results']
    for movie in movies:
        my_movie_model = {
            "model": "movies.movie",
            "fields": {
                "title": "",
                "overview":"",
                "release_date": None,
                "poster_path": "",
                "vote_count":"",
                "vote_average":"",
                "genres":"",
                "tmdb_pk" :"",
            
            }
        }
        my_movie_model["fields"]["title"] = movie["title"]
        my_movie_model["fields"]["overview"] = movie["overview"]
        if movie.get("release_date"):
            my_movie_model["fields"]["release_date"] = movie.get("release_date")

        my_movie_model["fields"]["poster_path"] = movie["poster_path"]
        my_movie_model["fields"]["vote_count"] = movie["vote_count"]
        my_movie_model["fields"]["vote_average"] = movie["vote_average"]
        my_movie_model["fields"]["genres"] = movie["genre_ids"]
        my_movie_model["fields"]["tmdb_pk"] = movie["id"]

        my_db_data.append(my_movie_model)


movie_json_file = open("./movies/fixtures/movies.json","w")
json.dump(my_db_data, movie_json_file, indent= 4)
movie_json_file.close()