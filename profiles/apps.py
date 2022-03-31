from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
    
    #apps filedinda ready function ile signali register etmeliyem
    def ready(self):
        import profiles.signals
