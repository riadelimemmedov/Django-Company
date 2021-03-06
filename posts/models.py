from django.db import models
from django.core.validators import FileExtensionValidator
from reports.models import Report,ProblemReported
from profiles.models import Profile
from django.urls import reverse
import uuid
import os
# Create your models here.


LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike')
)

#!PostManager Model Manager
class PostManager(models.Manager):
    def public_only(self):
        return self.filter(problem_reported__public=True)

#!Post Model
class Post(models.Model):
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    liked = models.ManyToManyField(Profile,related_name='liked_prof',blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    @property
    def num_likes(self):
        return self.liked.all().count()

#!ProblemPost Model 
class ProblemPost(Post):
    report = models.ForeignKey(Report,on_delete=models.CASCADE)
    problem_reported = models.ForeignKey(ProblemReported,on_delete=models.CASCADE)
    
    objects = PostManager()
    
    def __str__(self):
        return '{}'.format(self.problem_reported.description[:50])
    
    def get_absolute_url(self):
        return reverse('posts:pp-detail',kwargs={'pk1':self.pk,'pk':self.problem_reported.id})


#*get_upload_path
def get_upload_path(instance,filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4(),ext)
    return os.path.join('uploads/posts/img',filename)

#!GeneralPost Model
class GeneralPost(Post):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=350)
    image = models.ImageField(blank=True,upload_to=get_upload_path,validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    
    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('posts:gp-detail',kwargs={'pk':self.pk})
    
#!Like Model
class Like(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    value = models.CharField(max_length=50,choices=LIKE_CHOICES,default='Like')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.post)

#!Comment
class Comment(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(GeneralPost,on_delete=models.CASCADE,related_name='comments')
    body = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{}".format(str(self.pk))
    
    class Meta:
        ordering = ['-created']
        