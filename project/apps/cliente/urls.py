from django.urls import path
from .views import home, crear_clientes, crear_cliente, busqueda #! Importación de la función home en views.py

app_name = "cliente"

urlpatterns = [
    path("", home, name="home"),
    path("crear_clientes", crear_clientes, name="crear_clientes"),
    path("crear/", crear_cliente, name="crear"), 
    path("busqueda", busqueda, name="busqueda"),
]