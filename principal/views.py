from django.shortcuts import render, render_to_response, get_object_or_404
# importar los modelos
from principal.models import Receta, Comentario
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import RequestContext

# importar el usuario

# Create your views here.


# crear una vista de ejemplo sobre:

def Sobre(request):
    html = "<html> <body> <h1> Proyecto de Recetas </h1> </body></html>"
    return HttpResponse(html)


# la vista debe retornar todos los objetos existentes de recetas

def Inicio(request):
    recetas = Receta.objects.all()
    return render_to_response('principal/inicio.html', {'recetas': recetas}, context_instance=RequestContext(request))
