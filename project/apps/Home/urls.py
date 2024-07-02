from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

app_name = "Home"

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout ,name="logout"),
    path("register/", views.register, name="register"),
]  

urlpatterns += staticfiles_urlpatterns()