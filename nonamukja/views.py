from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from .models import Post
from .serializers import PostSerializer

class PostListCreateView(ListCreateAPIView):

    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer
