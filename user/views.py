import json
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.views import TokenObtainPairView

from user.serializers import UserSerializer
from user.models import User
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = User.objects.get(email=request.data.get("email"))
        user_information = {
            "token": response.data["access"],
            "username": user.username,
            "email": user.email,
            "user_id": user.id,
            "image": None,
            "bio": None
        }
        return JsonResponse({'user': user_information}, status=status.HTTP_200_OK)
        # return user_information

# Create your views here.
class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            user = serializer.save()
            
            return JsonResponse({
                'message': 'Register successful!'
            }, status=status.HTTP_201_CREATED)

        else:
            return JsonResponse({
                'error_message': 'This email has already exist!',
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)
        
class UserProfile(APIView):
    def get(sefl, request):
        user = request.user
        print("user: ", request.headers)
        user = User.objects.get(email=user)
        user_information = {
            "username": user.username,
            "email": user.email,
            "image": None,
            "bio": None
        }
        return JsonResponse({'user': user_information}, status=status.HTTP_200_OK)

class CheckServer(APIView):
    def get(sefl, request):
        return JsonResponse({
                'status': 'OK'
            }, status=status.HTTP_200_OK)