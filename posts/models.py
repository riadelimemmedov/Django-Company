from wsgiref.validate import validator
from django.db import models
from django.core.validators import FileExtensionValidator
import uuid
import os
from reports.models import *
from profiles.models import *
# Create your models here.

#!Post Model
class Post(models.Model):
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    liked = models.ManyToManyField(Profile,related_name='liked_prof',blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    @property# => burda yeni funksiyanin ustunde => @property decoratorundan istifade olunmasindaki sebeb biz yazilan funksiyani cagiranda () acmag kimi yox deyisken kimi istifade etmek isteyirik ona gorede => @property decoratorlarindan istifade olunur
    def num_likes(self):
        return self.liked.all().count()

#!ProblemPost Model 
class ProblemPost(Post):#bu model tempplatede gorunenden kenarlari mavi rengde gorunecek
    report = models.ForeignKey(Report,on_delete=models.CASCADE)
    problem_reported = models.ForeignKey(ProblemReported,on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}'.format(self.problem_reported.description[:50])


#*get_upload_path
def get_upload_path(instance,filename):
    ext = filename.split('.')[-1]#yeni noqteye gore parcalayib -1 deyerini aliriq yeni sondaki deyerini
    filename = '{}.{}'.format(uuid.uuid4(),ext)
    return os.path.join('uploads/posts/img',filename)

#!GeneralPost Model
class GeneralPost(Post):#bu model templatede gorunende kenarlari qirmizi seklinde gorunecek ve hami bu model ile post yaza biler ve paylasa biler
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=350)
    image = models.ImageField(blank=True,upload_to=get_upload_path,validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    
    def __str__(self):
        return str(self.title)