from django.http import HttpResponse #! Importación
# from django.template import Context, Template

def saludar(request):
    return HttpResponse("Hola Mundo")

def nombre(request, nombre, apellido):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"Hola {nombre} {apellido}")

def template(request):
    #mi_html = open("./templates/template1.html")
    #mi_template = Template(mi_html.read())
    #mi_html.close()
    #mi_context = Context()
    #mi_documento = mi_template.render(mi_context)
    #return HttpResponse(mi_documento)
    