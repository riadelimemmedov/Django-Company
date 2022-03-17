from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import random
from categories.models import *
from products.models import *
from django.urls import reverse
from django.db.models import Sum
from areas.models import *

# Create your models here.


########################################################################################################

#!Report Model
hours = ([(str(x),str(x)) for x in range(1,25)])
el = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#!ReportQueryset
class ReportQueryset(models.QuerySet):
    
    def filter_by_day_prodid(self,day,prod_id):
        return self.filter(day=day,production_line__id=prod_id)
    
    def aggregate_execution(self):
        return self.aggregate(Sum('execute'))
    
    def aggregate_plan(self):
        return self.aggregate(Sum('plan'))

#!ReportManager
class ReportManager(models.Manager):
    
    #get_queryset
    def get_queryset(self):
        return ReportQueryset(self.model,using=self._db)
    
    #filter given day
    def filter_by_day_prodid(self,day,prod_id):
        return self.get_queryset().filter_by_day_prodid(day,prod_id)
    
    #return all execute sum in database
    def aggregate_execution(self):
        return self.get_queryset().aggregate_execution()
    
    #return all plan sum in database
    def aggregate_plan(self):
        return self.get_queryset().aggregate_plan()
    
################################################################################################################################

#!Yeni hesabat verme modelidir bu her hansi bir PRODUCT haqqinda
class Report(models.Model):
    day = models.DateField(default=timezone.now)
    start_hour = models.CharField(max_length=2,choices=hours)#yeni bu isi bu saat araliginda gormlelisen kimi  
    end_hour = models.CharField(max_length=2,choices=hours)#
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    plan = models.PositiveSmallIntegerField() #plan yeni planama yeni meselen 200 dene mal gelmelidir
    execute = models.PositiveBigIntegerField() #execute etmek yeni icra etmek reportu,execute ise meselen 200 mal gelmelidir amma biz 180 getirmirik hazir elemisik yeni
    production_line = models.ForeignKey(ProductionLine,on_delete=models.CASCADE) #yeni harda emal olundugunu gosteren yer
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    #ReportManager
    objects = ReportManager()
    
    def __str__(self):
        return "{}-{}-{}".format(self.start_hour,self.end_hour,self.production_line)
    
    def get_day(self):
        return self.day.strftime('%Y/%m/%d')#strftime sayesinde zamani duzeleyirsen yeni neler gorunsun gelen tarix icinde onu qeyd edirsen strftime sayesinde
    
    def get_absolute_url(self):
        return reverse('pform:reportUpdatView',kwargs={'production_line':self.production_line,'pk':self.pk})
    
    class Meta:
        ordering = ['-created']
        
#!Random Code Function
def random_code():
    random.shuffle(el)
    code = [str(x) for x in el[:12]]#yeni 12 elemt icinden donsun butun element icinde yox bunun ucunde => el[:12]
    str_code = ''.join(code)#joini ''.join seklinde yazanda listdeki datta olsun yada ferq elemir neyse yan yana yazir nececi biz sozleri yazmirig ele => ''.join sayesinde
    return str_code
random_code()

#!ProblemReported Model
class ProblemReported(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)#Categroy Model
    description = models.TextField()
    problem_id = models.CharField(max_length=12,unique=True,blank=True,default=random_code)#funksiyani cagirmirsan burda sadece tetikleyirse Js deki eventler kimi
    breakdown = models.PositiveIntegerField()
    public = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    report = models.ForeignKey(Report,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{}-{}".format(self.category.name,self.description[:20])
    
    class Meta:
        verbose_name = 'Problem Reported'
        verbose_name_plural = 'Problems Reported'