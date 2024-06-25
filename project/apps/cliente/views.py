from .models import Cliente #! Importación 
from django.shortcuts import render 

def home(request): #! Importada a urls
    clientes_registrados = Cliente.objects.all() #! Objects.all consulta a la base de datos y trae todos los registros
    return render(request, "cliente/index.html", {"clientes": clientes_registrados})
                                         #! HTML
