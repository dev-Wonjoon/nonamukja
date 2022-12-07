from django.db import models
from rest_framework import serializers
from .models import Post
from datetime import datetime
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.models import User

class PostSerializer(serializers.ModelSerializer):

    def create(self, validated_data):


        post = Post(
            title = self.validated_data['title'],
            content = self.validated_data['content'],
            photo = self.validated_data['photo'],
            writer = self.validated_data['writer'],
        )
        post.save()
        return post

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()
        return instance


    class Meta:
        model = Post
        fields = ['pk', 'title', 'content', 'photo', 'created_at', 'updated_at', 'writer']


