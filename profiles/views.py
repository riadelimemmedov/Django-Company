from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import *
# Create your views here.

def test_view(request):
    print('Succses response test_view url')
    return HttpResponse("Successfully Response test_view")

def test_view1(request):
    return HttpResponse('Go to sleep')

def test_view2(request):
    if request.user.is_authenticated:
        user = request.user#gelen useri database gonder ve yoxla
        profile = Profile.objects.get(user=user)
    else:
        profile = "no found user"
    
    context = {
        'profile':profile,
    }
    return render(request,'profiles/test.html',context)