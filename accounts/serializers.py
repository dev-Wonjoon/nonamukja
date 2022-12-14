from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(email=validated_data["email"], nickname=validated_data["nickname"])
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['pk', 'email', 'password', 'nickname']

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['pk', 'email', 'password', 'nickname']
        read_only_fields = ['email']
