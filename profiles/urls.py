from tkinter.filedialog import test
from django.urls import path
from .views import *

app_name = 'profiles' #app_nem deyeri beraberdi root urlde olan namespace deyerine

urlpatterns = [
    path('',profileView,name='profileView'),
    # path('gtslepp/',test_view1,name='test_view1'),
    # path('testviewtemplate/',test_view2,name='test_view2'),
]