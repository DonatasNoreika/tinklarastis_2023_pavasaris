from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="posts"),
    path("posts/<int:pk>", views.PostDetailView.as_view(), name='post'),
    path('posts/new', views.PostCreateView.as_view(), name='post_new'),
]