from django.db import models
from products.models import *
from profiles.models import *

# Create your models here.

#!ProductionLine Models => O isi gorurku malin hazirlanmasindaki team ve bu malin hazirlanmasinda istifade olunann mallari burda qeyd edirik
class ProductionLine(models.Model):#yeni burani firma adi kimide dusunmek olar
    name = models.CharField(max_length=120)
    team_leader = models.ForeignKey(Profile,on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    
    def __str__(self):
        return str(self.name)