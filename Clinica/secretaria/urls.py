from django.urls import path
from . import views

app_name = "secretaria"

urlpatterns = [
    path("",views.home,name="home"),
    path("pacientes",views.pacientes,name="pacientes"),
    path("productos",views.productos,name="productos"),
    path("ventas",views.ventas,name="ventas"),
]