from os import name
from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('board/',PostListCreateView.as_view(),name='post-list-create'),
    path('like-unlike/',like_unlike_post,name='like-unlike-post'),
]