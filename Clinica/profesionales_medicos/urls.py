from django.urls import path
from . import views

app_name = "profesionales_medicos"

urlpatterns = [
    path("",views.home,name="home"),
    path("pacientes",views.pacientes,name="pacientes"),
]