from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#!Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(blank=True)
    website = models.CharField(max_length=220)#as an alternative if you can write in => models.URLField
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{}".format(self.user)