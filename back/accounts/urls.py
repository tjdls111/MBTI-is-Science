from django.urls import path
from . import views

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('',views.user_cud),
    path('mbti_change/',views.mbti_change),
    path('api-token-auth/', obtain_jwt_token),
    path('set_mbti/', views.set_mbti),
    path('pick_profile/', views.pick_profile),
    path('<user_name>/', views.profile),
    path('<user_name>/follow/',views.follow),
    path('<user_name>/is_follow/',views.is_follow),
]
