from django.urls import path
from .views import home #! Importación de la función home en views.py

app_name = "cliente"

urlpatterns = [
    path("", home, name="home"),
]