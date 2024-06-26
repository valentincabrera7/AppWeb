from .models import Cliente, Pais #! Importación 
from django.shortcuts import render, redirect
from datetime import date # datefield()

def home(request): #! Importada a urls
    clientes_registrados = Cliente.objects.all() #! Object.all LLAMADO A LA BASE DE DATOS
    contexto = {"clientes": clientes_registrados}
    return render(request, "cliente/index.html", contexto)
                                         #! HTML

def crear_cliente(request):
    p1 = Pais(nombre="Colombia")
    p2 = Pais(nombre="Perú")
    p3 = Pais(nombre="Brasil")
    p4 = Pais(nombre="Venezuela")

    p1.save()
    p2.save()
    p3.save()
    p4.save()

    c1 = Cliente(nombre = "Valentin", apellido = "Gonzalez", nacimiento = date(2000,1,1),pais_origen_id = p1)  
    c2 = Cliente(nombre = "Belen", apellido = "Tano", nacimiento = date(2000,1,1),pais_origen_id = p2)
    c3 = Cliente(nombre = "Luis", apellido = "Mario", nacimiento = date(2000,1,1),pais_origen_id = p3)
    c4 = Cliente(nombre = "Carlos", apellido = "Perez", nacimiento = date(2000,1,1),pais_origen_id = None)

    c1.save()
    c2.save()
    c3.save()
    c4.save()
    return redirect("cliente:home") #! APP_NAME Y PATH EN URLS

