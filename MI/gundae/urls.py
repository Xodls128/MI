from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('calendar/events/', views.event_data, name='event_data'),  # 이벤트 데이터를 위한 URL
]