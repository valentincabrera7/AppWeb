from django.urls import path
from . import views #! Importación de la función home en views.py

app_name = "producto"

urlpatterns = [
    path("", views.index, name="home"), 
    path("productocategoria/list/", views.productocategoria_list, name="productocategoria_list"),

]