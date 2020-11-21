from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "profesionales_medicos/home.html")

def pacientes(request):
    return render(request, "profesionales_medicos/pacientes.html")
