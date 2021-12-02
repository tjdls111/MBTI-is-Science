from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list_or_create),
    path('sort/<int:sort_pk>/', views.article_list_sort),
    path('<int:article_pk>/', views.article_detail),
    path('<int:article_pk>/comments/', views.comment_create),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('<int:article_pk>/likes/', views.like),
    path('<int:article_pk>/is_like/', views.is_like),
    path('<int:article_pk>/bookmark/', views.bookmark),
    path('<int:article_pk>/is_bookmark/', views.is_bookmark),
    path('<str:article_keyword>/search/', views.search),
    path('<str:author_name>/author_search/', views.author_search),

]
