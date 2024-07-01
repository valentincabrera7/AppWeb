from django.shortcuts import render 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.http.request import HttpRequest
from . import forms
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    return render(request, "Home/index.html")

#! LOGIN - LOGOUT

def login_request(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, "Home/index.html", {"mensaje": "Inició sesión correctamente"})
    else:
        form = forms.CustomAuthenticationForm()
    return render(request, "Home/login.html", {"form": form})



#! REGISTRO 

@staff_member_required
def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("username")
            form.save()
            return render(request, "Home/index.html", {"mensaje": "Alumno creado exitosamente."})
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "Home/register.html", {"form": form})




