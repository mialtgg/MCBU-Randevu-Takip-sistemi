from django.apps import AppConfig


class HistoryLoginConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "history_login"
    def ready(self):
        import history_login.signals