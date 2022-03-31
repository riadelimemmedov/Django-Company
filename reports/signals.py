from django.db.models.signals import post_save
from django.dispatch import receiver
from posts.models import *
from profiles.models import *
from .models import *

@receiver(post_save,sender=ProblemReported)
def post_save_report(sender,instance,created,*args,**kwargs):
    if created:
        try:
            id_rep = instance.report.id
            rep = Report.objects.get(id=id_rep)
        except:
            rep = None
        
        if rep is not None:
            user = instance.user
            profile = Profile.objects.get(user=user)
            ProblemPost.objects.create(author=profile,report=rep,problem_reported=instance)
            
