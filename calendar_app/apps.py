from django.apps import AppConfig

class CalendarAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'calendar_app'

    def ready(self):
        # signals 사용 시 아래 줄을 추가
        # import calendar_app.signals  # 주석 처리
        pass
