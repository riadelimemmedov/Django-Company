from os import name
from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('',PostListCreateView.as_view(),name='post-list-create'),
    path('like-unlike/',like_unlike_post,name='like-unlike-post'),
    path('<pk>/detail/',GeneralPostDetail.as_view(),name='gp-detail'),
    path('<pk1>/<pk>/detail/',ProblemDetailPost.as_view(),name='pp-detail'),
    path('<pk>/delete/',GeneralPostDeleteView.as_view(),name='gp-delete')
]