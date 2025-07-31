from django.apps import AppConfig


class AtmpAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'praevia_app'
    
    def ready(self):
        import praevia_app.signals 
