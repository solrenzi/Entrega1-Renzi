from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#COMENTARIOS INTERNOS DEL GRUPO, ANTES DE ENTREGAR BORRARLOS!
#cuando creemos formularios y modelos recordar importarlos en este archivo de vistas

#Creo la vista inicio para ver que esta todo ok:
def inicio(request):
    return HttpResponse("Esto es una prueba de inicio")
    
    # return render(request, 'AppCoder/estadio.html')
