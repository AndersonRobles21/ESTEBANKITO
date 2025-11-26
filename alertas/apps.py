from django.apps import AppConfig


class AlertasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'alertas'
    def ready(self):
        # conectar señales que dependen de modelos de otras apps
        try:
            from . import signals  # noqa: F401
        except Exception:
            pass
