from django.urls import path
from . import views
from .views import calculate_score


urlpatterns = [
    path('', views.onepage_scroll, name='home'),  # 루트 디렉토리로 지정
    path('calculate-score/', calculate_score, name='calculate_score'),
]