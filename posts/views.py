from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse_lazy
from itertools import chain
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from profiles.models import *
from .mixins import *
from django.views.generic import *
# Create your views here.

#!ProblemDetailPost
class ProblemDetailPost(LoginRequiredMixin,DetailView):
    model = ProblemPost
    template_name = 'posts/post-detail.html'
    pk_url_kwarg = 'pk1'#functio based with as pk in at second parametr pass in functio get url id
    

#!GeneralPostDetail
class GeneralPostDetail(LoginRequiredMixin,DetailView):
    model = GeneralPost
    template_name = 'posts/post-detail.html'
    
    #?Returns the single object that this view will display
    def get_object(self,*args,**kwargs):#yeni objecte get,tut onu,al yeni
        pk = self.kwargs.get('pk')
        post_ = get_object_or_404(GeneralPost,pk=pk)
        return post_

    #?Return context data at template tha is html template
    def get_context_data(self,**kwargs):
        context = super(GeneralPostDetail,self).get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self,*args,**kwargs):
        profile = Profile.objects.get(user=self.request.user)
        post_ = self.get_object()
        form = CommentForm(self.request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = profile
            instance.post = post_
            instance.body = form.cleaned_data.get('body')
            form.save()
            #after save form redirect previous page redirect url => self.request.META.get('HTTP_REFERER') WITH
        return redirect(self.request.META.get('HTTP_REFERER'))#ozunden evvelki seyfeye donur
    

#!PostListCreateView
class PostListCreateView(FormUserRequiredMixin,CreateView):#createView den istifade etdiyimiz ucun yeni miras aldigimiz ucun pramoy uje post yaratma prosesi gedir burda
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