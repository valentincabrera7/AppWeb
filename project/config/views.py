from django.http import HttpResponse #! Importación

def saludar(request):
    return HttpResponse("Hola Mundo")