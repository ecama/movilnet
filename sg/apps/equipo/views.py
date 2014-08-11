from django.views.generic import CreateView, TemplateView, ListView
from .models import Equipo
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render 
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext


class RegistrarEquipo(CreateView):
	template_name = 'equipo/registrar_equipo.html'
	model = Equipo
	success_url = reverse_lazy('lista_equipos')

class BuscarView(TemplateView):

		def post(self, request, *args, **kwargs):
				buscar = request.POST['buscalo']
				equipos = Equipo.objects.filter(host_name__contains=buscar)
				if equipos:
					return render(request, 'equipo/buscar.html',
									{'especific':equipos ,'serial':True})
				elif equipos:
					especific = Equipo.objects.filter(serial__contains=buscar)
					return render(request, 'equipo/buscar.html',
									{'especific':especific ,'serial':True})

				else:
					modelo = Equipo.objects.filter(modelo__contains=buscar)
					return render(request, 'equipo/buscar.html',
									{'especific':modelo ,'serial':True})					

def lista_equipos(request):
	equiposs = Equipo.objects.all()
	return render_to_response('equipo/lista_equipos.html',{'lista_equipos':equiposs}, context_instance=RequestContext(request))

def detalle_equipo(request, id_equipo):
	dato = get_object_or_404(Equipo, pk=id_equipo)
	return render_to_response('equipo/equipo.html',{'equipo':dato}, context_instance=RequestContext(request))	




