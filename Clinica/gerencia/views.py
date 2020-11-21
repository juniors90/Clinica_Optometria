from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "gerencia/home.html")

def pacientes(request):
    return render(request, "gerencia/pacientes.html")

def productos(request):
    return render(request, "gerencia/productos.html")

def ventas(request):
    return render(request, "gerencia/ventas.html")


