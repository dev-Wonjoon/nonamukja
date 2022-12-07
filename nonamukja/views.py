from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Post
from accounts.models import User
from .serializers import PostSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication
from rest_framework_simplejwt.models import TokenUser

class PostListCreateView(APIView):

    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        header = JWTAuthentication.get_header(self, request=request)
        token = JWTAuthentication.get_raw_token(self, header)
        validated_token = JWTAuthentication.get_validated_token(self, token)
        user_email = JWTStatelessUserAuthentication.get_user(self, validated_token)
        print(type(user_email.pk))
        user = User.objects.get(email=user_email.pk)

        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

