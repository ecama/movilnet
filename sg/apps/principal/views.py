from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from apps.equipo.models import Equipo
from apps.ubicacion.models import Sede
from django.views.generic import ListView

#def Principal(request):
#    return render_to_response('principal/pagPrincipal.html', context_instance=RequestContext(request))

def Registro(request):
    return render_to_response('principal/registro.html', context_instance=RequestContext(request))


class Principal(ListView):
	template_name = 'principal/pagPrincipal.html'
	model = Equipo
	context_object_name = 'lista_equipos'