from django.shortcuts import render 

def home(request):
    contexto =  {"app": "Aplicación de Productos"}
    return render(request, "producto/index.html", contexto)