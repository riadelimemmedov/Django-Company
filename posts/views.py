from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from itertools import chain
from .models import *
from .forms import *
from profiles.models import *
from django.views.generic import *
# Create your views here.

#!PostListCreateView
class PostListCreateView(CreateView):
    template_name = 'posts/post-create-list.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:post-list-create')
    
    def get_context_data(self,*args,**kwargs):
        qs1 = ProblemPost.objects.public_only()
        qs2 = GeneralPost.objects.all()
        qs = sorted(chain(qs1,qs2),reverse=True,key=lambda obj:obj.created)
        context = super(PostListCreateView,self).get_context_data(*args,**kwargs)#context deyiskeninin yazmagi deyisken kimi tanitmagi unutma ve super yazmagida hemcinin
        context['object_list'] = qs
        return context
        
    
    #!?oldugun seyfeye geri donmek ucun deg get_success_url lerden istifade olunur
    # def get_success_url(self):
    #     return self.request.path
    
def like_unlike_post(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)
    
    like,created = Like.objects.get_or_create(user=profile,post=post_obj)

    print('Created Boolean Value Befere Conditions', created)#eger true dursa avtomatik like save isleyecek if not created serti islemeyecek
    
    if not created:#not created dirsa demeli bu evvelceden var
        print('Created Deyeri', created)
        if like.value == 'Like':
            like.value = 'Unlike'
        else:
            like.value = 'Like'
    like.save()
    return redirect('posts:post-list-create')