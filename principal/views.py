# coding: utf-8
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



# metodo que retorna todos los usuarios del sistema, las recetas registradas

def Usuarios(request):
    usuarios = User.objects.all()
    recetas = Receta.objects.all()
    titulo = "Página de usuarios y Recetas Registradas"

    return render_to_response('principal/usuarios.html',
                              {'usuarios': usuarios,
                               'recetas': recetas,
                               'titulo':titulo},
                              context_instance=RequestContext(request))

