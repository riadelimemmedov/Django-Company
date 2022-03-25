from django.contrib import admin
from .forms import *
from .models import *
# Register your models here.

class GeneralPostAdmin2(admin.ModelAdmin):
    form = PostForm

#!GeneralPostAdmin
class GeneralPostAdmin(admin.ModelAdmin):
    list_display = ['__str__','num_likes','author','created']
    exclude = ['liked']
    
    class Meta:
        model=GeneralPost

class ProblemPostAdmin(admin.ModelAdmin):
    list_display = ['__str__','num_likes','author','created']
    fields = ['author','report','problem_reported']
    list_display_links = ['__str__','author']
    list_filter = ['created']
    search_fields = ['author__user__username']

admin.site.register(ProblemPost,ProblemPostAdmin)
admin.site.register(GeneralPost,GeneralPostAdmin2)#!sonra deyis burani oz classi ver