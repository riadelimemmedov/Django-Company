from django.db import models

# Create your models here.

#!Product Model 
class Product(models.Model):
    name = models.CharField(max_length=220)
    short_code = models.CharField(max_length=20)
    description = models.TextField(blank=True,null=True) 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'