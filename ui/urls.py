from django.urls import path
from . import views

app_name = "ui"

urlpatterns = [
    path("", views.home, name="home"),
    path("urni/nuevo/", views.urni_crear, name="urni_crear"),
]
