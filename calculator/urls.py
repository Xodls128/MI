# calculator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('general/', views.general_technical_view, name='general_technical'),
    path('special/', views.special_technical_view, name='special_technical'),
]
