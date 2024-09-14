from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('calendar/events/', views.event_data, name='event_data'),  # 이벤트 데이터를 위한 URL
    path('general/', views.general_technical_view, name='general_technical'),
    path('special/', views.special_technical_view, name='special_technical'),
]