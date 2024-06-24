from django.http import HttpResponse #! Importación
# from django.template import Context, Template #! ANTES
from django.shortcuts import render #! Importación #! AHORA
 
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
    #mi_context = Context()
    #mi_documento = mi_template.render(mi_context)
    #return HttpResponse(mi_documento)
    #! AHORA 
    return render(request, "template1.html")
    


    
    
