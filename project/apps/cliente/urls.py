from django.urls import path
from .views import home, crear_cliente #! Importación de la función home en views.py

app_name = "cliente"

urlpatterns = [
    path("", home, name="home"),
    path("crear_cliente", crear_cliente, name="crear_cliente"),
]