from django.contrib.auth import get_user_model
from django.db import models
from rest_framework import serializers
from .models import Post
from datetime import datetime
from accounts.models import User
from accounts.serializers import UserSerializer

class AuthorSerialier(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["email", "nickname"]

class PostSerializer(serializers.ModelSerializer):

    writer = AuthorSerialier(read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()
        return instance


    class Meta:
        model = Post
        fields = ['pk', 'title', 'content', 'talk_link', 'photo', 'created_at', 'updated_at', 'writer']
        read_only_fields = ['writer']


