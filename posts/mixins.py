from django import forms
from profiles.models import *

#!FormUserRequiredMixin
class FormUserRequiredMixin(object):
    def form_valid(self,form):
        if self.request.user.is_authenticated:
            profile = Profile.objects.get(user=self.request.user)
            form.instance.author = profile
            #if succes form return together with based class template
            return super(FormUserRequiredMixin,self).form_valid(form)
        else:
            form.add_error(None,'User Must Be Logged In')
            return self.form_invalid(form)#that new if class return self.form_invalid(form),form rows must be return form.add_error(None,'error text')
        
        