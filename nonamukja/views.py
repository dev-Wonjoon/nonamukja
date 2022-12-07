from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Post
from .serializers import PostSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class PostListCreateView(APIView):

    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        header = JWTAuthentication.get_header(self, request=request)
        token = JWTAuthentication.get_raw_token(self, header)
        validated_token = JWTAuthentication.get_validated_token(self, token)
        user = JWTAuthentication.get_user(self, validated_token)
        print(user)
        serializer = PostSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

