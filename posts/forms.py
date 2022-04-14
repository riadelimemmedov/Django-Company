from django import forms
from django.core.validators import ValidationError
from .models import *

#!PostForm
class PostForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':'3'}))
    class Meta:
        model = GeneralPost
        fields = ['title','description','image']
    
    
    def clean_description(self):
        desc = self.cleaned_data.get('description')
        if(len(desc)<10):
            raise forms.ValidationError('Short Description')
        return desc

#!CommentForm
class CommentForm(forms.ModelForm):
    body = forms.CharField(label='',widget=forms.Textarea(attrs={'rows':'4','placeholder':'Your Comment'}))
    
    class Meta:
        model = Comment
        fields = ['body']