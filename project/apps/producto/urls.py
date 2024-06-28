from django.urls import path
from . import views #! Importación de la función en views.py
from django.views.generic import TemplateView

app_name = "producto"

urlpatterns = [
    path("", TemplateView.as_view(template_name="producto/index.html"), name="index"), 
    path("productocategoria/list/", views.ProductoCategoriaList.as_view(), name="productocategoria_list"),
    path("productocategoria/create/", views.ProductoCategoriaCreate.as_view(), name="productocategoria_create"),
    path("productocategoria/detail/<int:pk>", views.ProductoCategoriaDetail.as_view(), name="productocategoria_detail"),
    path("productocategoria/update/<int:pk>", views.ProductoCategoriaUpdate.as_view(), name="productocategoria_update"),
    path("productocategoria/delete/<int:pk>", views.ProductoCategoriaDelete.as_view(), name="productocategoria_delete"),
]