from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('order_by/<int:sort_pk>/', views.movie_list_sort),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/pick/', views.pick),
    path('<int:movie_pk>/is_pick/', views.is_pick),
    path('today_recommend/', views.today_recommend),
    path('<int:area>/today_recommend/', views.today_recommend_by),
    path('<str:mbti_name>/mbti_recommend/', views.mbti_recommend),
    path('<int:movie_pk>/movie_recommend/', views.movie_recommend),
    path('<int:movie_pk>/reviews/', views.reviews),
    path('<str:movie_keyword>/search/', views.search),
    path('<str:movie_pk>/actors/', views.actors),
    
]
