from django.shortcuts import render
from django.urls import reverse_lazy
from itertools import chain
from .models import *
from .forms import *
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
        context = super(PostListCreateView,self).get_context_data(*args,**kwargs)
        context['object_list'] = qs
        return context
        
        
    
    #!?oldugun seyfeye geri donmek ucun deg get_success_url lerden istifade olunur
    # def get_success_url(self):
    #     return self.request.path
