from .models import Cliente, Pais #! Importación 
from django.shortcuts import render, redirect
from .forms import ClienteForm #! Importación 
from datetime import date # datefield()
from django.http import HttpResponse, HttpRequest

def home(request): #! Importada a urls
    clientes_registrados = Cliente.objects.all() #! Object.all LLAMADO A LA BASE DE DATOS
    contexto = {"clientes": clientes_registrados}
    return render(request, "cliente/index.html", contexto)
                                         #! HTML

def crear_clientes(request):
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

def crear_cliente(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":  #! TRAE DATOS DEL FORMULARIO
        form = ClienteForm(request.POST) #! SE GUARDA EN EL FORMULARIO
        if form.is_valid():
            form.save() #! BASE DE DATOS
            return redirect("cliente:home") #! VOLVER A OTRA PAGINA PARA NO VOLVER A CREAR OTRO CLIENTE SI NO ES NECESARIO
    else: # request.method == "GET":
        form = ClienteForm()
    return render(request, "cliente/crear.html", {"form": form})
        
def busqueda(request: HttpRequest) -> HttpResponse:
    # BUSQUEDA POR NOMBRE
    cliente_nombre = Cliente.objects.filter(nombre__contains="Valentin")

    # BUSQUEDA POR FECHA DE NACIMIENTO > 2000
    cliente_nacimiento = Cliente.objects.filter(nacimiento__gt=date(2000,1,1))

    # BUSQUEDA POR PAIS DE ORIGEN VACIO
    cliente_pais = Cliente.objects.filter(pais_origen_id=None)

    contexto = {"cliente_nombre": cliente_nombre, 
                "cliente_nacimiento": cliente_nacimiento,
                "cliente_pais": cliente_pais}
    return render(request, "cliente/busqueda.html", contexto)

