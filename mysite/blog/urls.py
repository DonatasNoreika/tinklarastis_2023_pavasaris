from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="posts"),
    path("posts/<int:pk>", views.PostDetailView.as_view(), name='post'),
    path('posts/new', views.PostCreateView.as_view(), name='post_new'),
    path('posts/<int:pk>/update', views.PostUpdateView.as_view(), name="post_update"),
    path('posts/<int:pk>/delete', views.PostDeleteView.as_view(), name='post_delete'),
    path('posts/<int:pk2>/comments/<int:pk>/update', views.CommentUpdateView.as_view(), name='comment_update'),
    path('posts/<int:pk2>/comments/<int:pk>/delete', views.CommentDeleteView.as_view(), name='comment_delete'),
]