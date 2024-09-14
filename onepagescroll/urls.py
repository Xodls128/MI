from django.urls import path
from . import views

urlpatterns = [
    path('', views.onepage_scroll, name='home'),  # 루트 디렉토리로 지정
]