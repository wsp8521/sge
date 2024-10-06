from django.apps import AppConfig


class SgeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sge'
    
     #habilitando signals na aplicação
    def ready(self):
        import sge.signals
