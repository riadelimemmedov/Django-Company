from django import forms
from django.core.validators import ValidationError
from .models import *

#!PostForm
class PostForm(forms.ModelForm):#eger forms.Form yazsagdig sifirdan her bir setri yeni rowu kodlamag lazi idi eger ferqli bir form yaradirigsa,amma forms.ModelForm database deki table gore yaradir formu amm class meta icinde hemin model clasini qeyd etmelinse yeni => class Meta:model=TableAdi
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':'3'}))#widget yerine girdinse demeli uje html yazirsan kimi bir seydi diqqetli ol burda
    class Meta:
        model = GeneralPost
        fields = ['title','description','image']
    
    
    #?burda basina clean yazilmasindaki sebeb hemin field in ustunden gostersin erroru ona gore yeni clean_description,description bizim field mizin adidir cleanda yazib evveline altdan xett ile ayiranda yeni deyirikki bu fieldde xeta olanda bu fielin ustunde goster yalniz xetani,yeni general error vermir,custom error verir bu cur yazilis her bir field in ozun mexsus error yeni
    #?yeni isare edir burda clean_fieldadi ki yeni yalniz burdaki xetalari tut menasindan fe hemin field icinde goster menasinda
    def clean_description(self):#class icinde oldugumuz ucun self keywordunu yazmlayigki class icinde attributlari istifade ede bilek
        desc = self.cleaned_data.get('description')
        if(len(desc)<10):
            #raise ValueError('Description Too Short')
            #!ve ya
            raise forms.ValidationError('Short Description')#bu yol daha yaxsidir
            #!ve ya
            #raise ValidationError('Description Errror Short Lenght')
        #else kimidir bura yeni
        return desc