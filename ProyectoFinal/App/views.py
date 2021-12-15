from django.shortcuts import render
from django.http import HttpResponse
from App.models import Ciudades, Restaurantes, Alojamientos


# Create your views here.


def inicio(request):
    #return HttpResponse("Esto es una prueba de inicio") - Ok funciono
    
    return render(request, 'App/inicio.html')

def ciudades(request):
 
    return render(request, 'App/ciudades.html')

def restaurantes(request):
    
    return render(request, 'App/restaurantes.html')

def alojamientos(request):
    
    return render(request, 'App/alojamientos.html')

def dejaTuComentario(request):
    
    return render(request, 'App/dejaTuComentario.html')

def alojamientoFormulario(request):
    
    return render(request, 'App/alojamientoFormulario.html')
    
    
    
    
