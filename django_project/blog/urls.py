from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView,
    UserPostListView,
)
from . import views


app_name = "blog"
urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('user/<str:username>', UserPostListView.as_view(), name='user_posts'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<str:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<str:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<str:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]