from django.shortcuts import render 

def home(request):
    return render(request, "Home/index.html", {"saludo": "Hola Mundo"})