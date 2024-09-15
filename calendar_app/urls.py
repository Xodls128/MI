from django.urls import path
from . import views


urlpatterns = [
    path('calendar/', views.calendar_view, name='calendar'),
    path('calendar/events/', views.event_list, name='event-list'),
    path('calendar/add/', views.add_event, name='add-event'),
]


