from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LogoutView

app_name = "Home"

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_request, name="login"),
    path("logout/", LogoutView.as_view(template_name="Home/logout.html"), name="logout"),
]  

urlpatterns += staticfiles_urlpatterns()