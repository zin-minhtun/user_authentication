from django.urls import path
from . import views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView, 
    UserPostListView
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog_home'),
    path('user_posts/<str:username>/', UserPostListView.as_view(), name='blog_user_posts'),
    path('post/create/', PostCreateView.as_view(), name='blog_create'),
    path('post/<int:pk>/detail/', PostDetailView.as_view(), name='blog_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='blog_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='blog_delete'),
    path('about/', views.about, name='blog_about')
]
