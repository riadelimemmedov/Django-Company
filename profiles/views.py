from django.shortcuts import render
from django.http import HttpResponse,Http404
from .forms import *
from .models import *
# Create your views here.


def profileView(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None
        
    form = ProfileModelForm(request.POST or None,request.FILES or None,instance=profile)
    
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.bio = form.cleaned_data.get('bio')
            instance.website = form.cleaned_data.get('website')
            instance.profile_picture = form.cleaned_data.get('profile_picture')
            form.save()
    
    context = {
        'profile':profile,
        'form':form
    }
    
    return render(request,'profiles/profile.html',context)



# def test_view(request):
#     print('Succses response test_view url')
#     return HttpResponse("Successfully Response test_view")

# def test_view1(request):
#     return HttpResponse('Go to sleep')

# def test_view2(request):
#     if request.user.is_authenticated:
#         user = request.user#gelen useri database gonder ve yoxla
#         profile = Profile.objects.get(user=user)
#     else:
#         profile = "no found user"
    
#     context = {
#         'profile':profile,
#     }
#     return render(request,'profiles/test.html',context)