from django.db import models
from profiles.models import Profile
from products.models import *

# Create your models here.

class ProductionLine(models.Model):
    name = models.CharField(max_length=120)
    team_leader = models.ForeignKey(Profile,on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    
    def __str__(self):
        return str(self.name)