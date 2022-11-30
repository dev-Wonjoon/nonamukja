from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['pk', 'title', 'content', 'photo', 'created_at', 'updated_at', 'writer']
        read_only_fields= ['created_at', 'updated_at']
