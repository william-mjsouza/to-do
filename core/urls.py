# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),  # Rota para a página inicial
]