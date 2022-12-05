from django.db import models
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    def create(request, validated_data):

        post = Post(
            title = validated_data['title'],
            content = validated_data['content'],
            photo = validated_data['photo'],
            writer = request.user
        )

        post.save()
        return post

    def get(self, request):
        pass

    class Meta:
        model = Post
        fields = ['pk', 'title', 'content', 'photo', 'created_at', 'updated_at', 'writer']
        read_only_fields= ['created_at', 'updated_at']
