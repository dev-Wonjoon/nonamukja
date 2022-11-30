from django.urls import path
from .views import PostListCreateView

urlpatterns = [
    path('post', PostListCreateView.as_view()),
]
