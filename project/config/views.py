from django.http import HttpResponse #! Importación

def saludar(request):
    return HttpResponse("Hola Mundo")

def nombre(request, nombre, apellido):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"Hola {nombre} {apellido}")