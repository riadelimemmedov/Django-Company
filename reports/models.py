from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import random
from categories.models import *
from products.models import *
from django.urls import reverse
from django.db.models import Sum,Avg
from datetime import datetime
from areas.models import ProductionLine

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
        return self.aggregate(Avg('execute'))
    
    def aggregate_plan(self):
        return self.aggregate(Avg('plan'))

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
    start_hour = models.CharField(max_length=2,choices=hours)  
    end_hour = models.CharField(max_length=2,choices=hours)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    plan = models.PositiveSmallIntegerField()
    execute = models.PositiveBigIntegerField()
    production_line = models.ForeignKey(ProductionLine,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    #ReportManager
    objects = ReportManager()
    
    def __str__(self):
        return "{}-{}-{}".format(self.start_hour,self.end_hour,self.production_line)
    
    def get_day(self):
        return self.day.strftime('%Y/%m/%d')
    
    def get_absolute_url(self):
        return reverse('pform:reportUpdatView',kwargs={'production_line':self.production_line,'pk':self.pk})
    
    class Meta:
        ordering = ['-created']



################################################################################


#!Random Code Function
def random_code():
    random.shuffle(el)
    code = [str(x) for x in el[:12]]
    str_code = ''.join(code)
    return str_code
random_code()

#!ProblemReportedManager

class ProblemReportedManager(models.Manager):
    
    def get_problems_by_day_and_line(self,day,line):
        return super().get_queryset().filter(report__day=day,report__production_line__name=line)

    def problems_from_today(self):
        now = datetime.now().strftime('%Y-%m-%d')
        return super().get_queryset().filter(report__day=now)
    
#!ProblemReported Model
class ProblemReported(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)#Categroy Model
    description = models.TextField()
    problem_id = models.CharField(max_length=12,unique=True,blank=True,default=random_code)
    breakdown = models.PositiveIntegerField()
    public = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    report = models.ForeignKey(Report,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    objects = ProblemReportedManager()
    
    def __str__(self):
        return "{}-{}".format(self.category.name,self.description[:20])
    
    class Meta:
        verbose_name = 'Problem Reported'
        verbose_name_plural = 'Problems Reported'