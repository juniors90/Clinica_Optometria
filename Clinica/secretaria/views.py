from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "secretaria/home.html")

def pacientes(request):
    return render(request, "secretaria/pacientes.html")

def productos(request):
    return render(request, "secretaria/productos.html")

def ventas(request):
    return render(request, "secretaria/ventas.html")