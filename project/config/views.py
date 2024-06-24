from django.http import HttpResponse 
# from django.template import Context, Template #! ANTES
from django.shortcuts import render #! AHORA
 
def saludar(request):
    return HttpResponse(request, "Hola Mundo")

def nombre(request, nombre, apellido):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"Hola {nombre} {apellido}")

def template(request):
    #! ANTES
    #mi_html = open("./templates/template1.html")
    #mi_template = Template(mi_html.read())
    #mi_html.close()
    #mi_contexto = Context(datos)
    #mi_documento = mi_template.render(mi_contexto)
    #return HttpResponse(mi_documento)

    #! AHORA
    #! VARIABLES PARA TEMPLATES
    nombre = "Luis" #! CONTEXTO PARA TEMPLATES
    apellido = "Perez" #! CONTEXTO PARA TEMPLATES
    datos = {"nombre": nombre, "apellido": apellido}
    return render(request, "template1.html", datos)


def notas(request):
    notas = [5, 10, 7]
    contexto = {"notas": notas}
    return render(request, "notas.html", contexto)


    




    
    
