from tkinter.filedialog import test
from django.urls import path
from .views import *

app_name = 'profiles'

urlpatterns = [
    path('',profileView,name='profileView'),
    # path('gtslepp/',test_view1,name='test_view1'),
    # path('testviewtemplate/',test_view2,name='test_view2'),
]