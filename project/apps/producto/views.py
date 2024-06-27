from django.shortcuts import render 
from . import models

#! PÁGINA PRINCIPAL 

def index(request):
    return render(request, "producto/index.html")


# LISTAR PRODUCTOS

def productocategoria_list(request):
    categorias = models.ProductoCategoria.objects.all()
    contexto = {"categorias": categorias}
    return render(request, "producto/productocategoria_list.html", contexto)