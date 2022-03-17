from pyexpat import model
from django import forms
from django.shortcuts import get_object_or_404
from areas.models import *
from .models import *

#!ReportForm 
class ReportForm(forms.ModelForm):#modelForm yazilmasindaki sebeb databasedi table cekib bura getireciyik
    class Meta:
        model = Report
        #fields = '__all__'
        exclude = ['user','production_line']
        
    def __init__(self,*args,**kwargs):
        #print(kwargs)
        production_line = kwargs.pop('production_line',None)
        #print('bune amkkk',production_line)
        super().__init__(*args,**kwargs)    
        if production_line is not None:
            line = get_object_or_404(ProductionLine,name=production_line)
            self.fields['product'].queryset = line.products.all()

#!ProblemReportedForm
class ProblemReportedForm(forms.ModelForm):
    class Meta:
        model = ProblemReported 
        #fields = '__all__'
        exclude = ['user','report','problem_id']

#!ReportSelectLineForm
class ReportSelectLineForm(forms.Form):
    production_line = forms.ModelChoiceField(queryset=ProductionLine.objects.none(),label=False)#setirdir formdan gosterilen
    print('Production  Line',production_line)

    def __init__(self,logged_user,*args,**kwargs):
        self.user = logged_user
        print('Logged User',self.user)
        super(ReportSelectLineForm,self).__init__(*args,**kwargs)
        self.fields['production_line'].queryset = ProductionLine.objects.filter(team_leader__user__username = logged_user)#32 setirdeki production_line dir self.fields['production_line'] daki row yeni setir

#!ReportResultForm
class ReportResultForm(forms.Form):#eger forms.Form yazirsansa ancag yazdiginiz setirler gorunecek templatede yeni asagida yazdigimiz production_line ve day setirleri
    production_line = forms.ModelChoiceField(queryset=ProductionLine.objects.all())
    day = forms.CharField(widget=forms.DateTimeInput(
        attrs={'class': 'datepicker'}
    ))
