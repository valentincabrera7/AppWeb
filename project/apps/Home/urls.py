from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "Home"

urlpatterns = [
    path("", views.home, name="home"),
]   

urlpatterns += staticfiles_urlpatterns()