from django.urls import path
from ProyectoFinalApp import views


urlpatterns = [
    path('', views.home, name="Home"),
    path('aboutme/', views.aboutme, name="Aboutme"),
    
]

