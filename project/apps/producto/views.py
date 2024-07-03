from django.shortcuts import render, redirect
from . import models
from . import forms
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# PÁGINA PRINCIPAL
  
@login_required
def index(request):
    return render(request, "producto/index.html")


#! LISTAR CATEGORIA DE PRODUCTOS
# def productocategoria_list(request):
    #categorias = models.ProductoCategoria.objects.all()
    #contexto = {"categorias": categorias}
    #return render(request, "producto/productocategoria_list.html", contexto)
class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria

#! CREAR CATEGORIA DE PRODUCTOS
#def productocategoria_create(request):
    #if request.method == "POST":  #! En caso de guardar datos
        #form = forms.ProductoCategoriaForm(request.POST)
        #if form.is_valid():
            #form.save()
            #return redirect("producto:home")  #! Cambia esto al nombre correcto de la URL de redirección
    #else:
        #form = forms.ProductoCategoriaForm()  #! Muestra el formulario
    #return render(request, "producto/productocategoria_form.html", {"form": form})   
class ProductoCategoriaCreate(CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")



#! DETALLE DE CATEGORIA DE PRODUCTOS
#def productocategoria_detail(request, pk):
    #query = models.ProductoCategoria.objects.get(id=pk) #! Consulta a la base de datos
    #return render(request, "producto/productocategoria_detail.html", {"object": query})
class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria


#! ACTUALIZAR CATEGORIA DE PRODUCTOS
#def productocategoria_update(request, pk):
    #query = models.ProductoCategoria.objects.get(id=pk) #! Consulta a la base de datos
    #if request.method == "POST":  #! En caso de guardar datos
        #form = forms.ProductoCategoriaForm(request.POST, instance=query)
        #if form.is_valid():
            #form.save()
            #return redirect("producto:home") 
        #else:
            #form = forms.ProductoCategoriaForm(instance=query) 
        #return render(request, "producto/productocategoria_form.html", {"form": form})
class ProductoCategoriaUpdate(UpdateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")



#! ELIMINAR CATEGORIA DE PRODUCTOS
#def productocategoria_delete(request: HttpRequest, pk: int) -> HttpResponse:
    #query = models.ProductoCategoria.objects.get(id=pk)
    #if request.method == "POST":
        #query.delete()
        #return redirect("producto:productocategoria_list.html")
    #return render(request, "producto/productocategoria_confirm_delete.html", {"object": query})
class ProductoCategoriaDelete(DeleteView):
    model = models.ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")
    

##################################################################################################################################################

#! LISTAR PRODUCTOS 
class ProductoList(ListView):
    model = models.Producto
    success_url = reverse_lazy("producto:producto_list")


#! CREAR PRODUCTOS
class ProductoCreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:producto_list")

#! DETALLE DE PRODUCTOS
class ProductoDetail(DetailView):
    model = models.Producto    
    success_url = reverse_lazy("producto:producto_detail")

#! ACTUALIZAR PRODUCTOS
class ProductoUpdate(UpdateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:producto_list")

#! ELIMINAR PRODUCTOS
class ProductoDelete(DeleteView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:producto_list")

