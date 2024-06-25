from django.urls import path
from .views import home #! Importación de la función home en views.py

urlpatterns = [
    path("", home, name="home"),
]