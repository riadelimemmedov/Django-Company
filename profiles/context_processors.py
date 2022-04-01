from .models import Profile

#!profilePicView
def profilePicView(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            profile = Profile.objects.get(user=user)
            picprofile = profile.profile_picture
        except Profile.DoesNotExist:
            picprofile = None
        return {'picprofile': picprofile}
    return{}

#!getProfileView
def getProfileView(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            profile = Profile.objects.get(user=user)
        except:
            profile = None
        return{'profile':profile}
    return{}