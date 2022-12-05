from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import SignupSerializer, UserSerializer
from .models import User


class SignupView(CreateAPIView):
    model = get_user_model()
    serializer_class = SignupSerializer
    permission_classes = [
        AllowAny,
    ]

class UserListView(ListAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [
        IsAdminUser,
    ]
