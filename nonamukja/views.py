from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Post
from accounts.models import User
from .serializers import PostSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        user = User.objects.get(email=self.request.user.pk)
        serializer.save(writer=user)
        return super().perform_create(serializer)


