from django import forms
from .models import *

class ProfileModelForm(forms.ModelForm):#ModelForm yazilanda databasedeki table i miras ala bilirsen,forms.Form yazanda sifirdan bir form yaratmis kimi olursan ele bil
    #burda yazialn deyisken adlari ile Meta class icinde yazilan deyisken adlari eyni olmalidirki django templatede yeni html de tanisin bunlari
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
