from os import name
from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('board/',PostListCreateView.as_view(),name='post-list-create')
]