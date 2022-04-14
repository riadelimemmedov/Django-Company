from django import forms
from .models import *

class ProfileModelForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Few Words Abipout You...',
        'rows':'3'
    }))
    
    website = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'placeholder': 'Your Website'
    }))
    
    class Meta:
        model = Profile
        fields = ['bio','website','profile_picture']
