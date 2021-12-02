from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer,UserProfileSerializer

from django.contrib.auth import get_user_model

# Create your views here.

@api_view(['POST', 'DELETE', 'PUT'])
@permission_classes([AllowAny])
def user_cud(request):
    def signup():
        password = request.data.get('password')
        password_confirmation = request.data.get('passwordConfirmation')

        if password != password_confirmation:
            return Response({'error':'비밀 번호가 일치하지 않습니다.'}, status = status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data = request.data)

        if serializer.is_valid(raise_exception=True):
            user= serializer.save()

            user.set_password(request.data.get('password'))
            user.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def user_delete():
        if request.user.is_authenticated:
            request.user.delete() # 계정 삭제
            # 로그 아웃 - 어떻게?? 

            return Response({"detail" :f"{request.user.username}(이)가 삭제되었습니다."}, status = status.HTTP_204_NO_CONTENT)
        
        return Response({'detail':'로그인한 사용자만 계정 삭제할 수 있습니다..'}, status=status.HTTP_401_FORBIDDEN) 


    def user_update():

        if request.user.is_authenticated:
            user = request.user

            password = request.data.get('password')
            password_confirmation = request.data.get('passwordConfirmation')

            if password != password_confirmation:
                return Response({'error':'비밀 번호가 일치하지 않습니다.'}, status = status.HTTP_400_BAD_REQUEST)
            

            serializer = UserSerializer(user, data = request.data)

            if serializer.is_valid(raise_exception=True):
                serializer.save()

                if password:
                    user.set_password(password)
                    user.save()

                return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'detail':'로그인한 사용자만 계정 정보 수정을 할 수 있습니다..'}, status=status.HTTP_401_FORBIDDEN) 

    if request.method == 'POST':
        return signup()
    
    elif request.method == 'DELETE':
        return user_delete()
    
    elif request.method == 'PUT':
        return user_update()
    
@api_view(['POST'])
def mbti_change(request):
    user = request.user
    mbti = request.data["mbti"]
    user.mbti = mbti
    user.save()
    return Response({'detail':f'{user}의 mbti가 {mbti}로 변경되었습니다.'})


@api_view(['GET'])
def set_mbti(request):
    me = request.user
    mbti = me.mbti
    return Response({"mbti": mbti})

@api_view(['GET'])
@permission_classes([AllowAny])
def profile(request, user_name):
    person = get_object_or_404(get_user_model(), username=user_name)
    serializer = UserProfileSerializer(person)
    return Response(serializer.data)

@api_view(['POST'])
def follow(request, user_name):
    if request.user.is_authenticated:
        you = get_object_or_404(get_user_model(), username = user_name)
        me = request.user

        if you != me:
            if you.followers.filter(pk=request.user.pk).exists():
                you.followers.remove(me)
                return Response({'detail':f'{user_name} 회원을 팔로우 취소했습니다.'}, status=status.HTTP_200_OK)
            else:
                you.followers.add(me)
                return Response({'detail':f'{user_name} 회원을 팔로우했습니다.'}, status=status.HTTP_200_OK)
        return Response({'detail':'본인을 팔로우할 수 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'detail':'로그인한 사용자만 팔로우, 팔로잉 기능을 이용할 수 있습니다.'}, status=status.HTTP_401_FORBIDDEN) 


@api_view(['GET'])
def is_follow(request, user_name):
    you = get_object_or_404(get_user_model(), username = user_name)
    me = request.user

    followers_cnt = you.followers.count()
    followings_cnt = you.followings.count()

    if you.followers.filter(pk=request.user.pk).exists():
        return Response({'isFollow':'true', 'follower_cnt': followers_cnt, 'following_cnt' : followings_cnt})
    return Response({'isFollow': 'false', 'follower_cnt': followers_cnt, 'following_cnt' : followings_cnt})


@api_view(['POST'])
def pick_profile(request):
    me = request.user
    number = request.data["poster_number"]
    me.poster_number = number
    me.save()
    return Response({'detail':f'프로필이 {number}번으로 변경되었습니다.'})    


