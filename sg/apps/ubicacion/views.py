from django.views.generic import CreateView, ListView
from .models import Sede, Sala, Fila, Rack
from apps.equipo.models import Equipo
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render 
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

class RegistrarSede(CreateView):
	template_name = 'ubicacion/registrarSede.html'
	model = Sede
	success_url = reverse_lazy('registrar_sala')


class RegistrarSala(CreateView):
	template_name = 'ubicacion/registrarSala.html'
	model = Sala
	success_url = reverse_lazy('reportar_sala')

	
class ReportarSala(ListView):
	template_name = 'ubicacion/reportarSala.html'
	model = Sala
	context_object_name = 'lista_de_salas'


class ReportarSede(ListView):
	template_name = 'ubicacion/reportarSede.html'
	model = Sede
	context_object_name = 'lista_de_sedes'


def lista_de_salas_por_sede(request, id_sede):
	sedee = get_object_or_404(Sede, pk=id_sede)
	salas = Sala.objects.filter(sede=sedee)
	equipos_en_sede = Equipo.objects.filter(sede=sedee)
	return render_to_response('ubicacion/lista_de_salas_por_sede.html',{'sede':sedee,'salas':salas,'equipos_en_sede':equipos_en_sede},
	 context_instance=RequestContext(request))


def lista_de_equipos_por_sala(request, id_sala):
	sala = get_object_or_404(Sala, pk=id_sala)
	sede = Sede.objects.all()
	id_sede = sala.sede
	salas = Sala.objects.filter(sede=id_sede)
	equipos_en_sala = Equipo.objects.filter(sala=sala)
	filas = Fila.objects.filter(sala=sala)
	print filas
	return render_to_response('ubicacion/lista_de_equipos_por_sala.html',{'sala':sala,'sede':id_sede,'salas':salas,
		'equipos_en_sala':equipos_en_sala,'filas':filas},
	 context_instance=RequestContext(request))


def lista_de_equipos_por_fila(request, id_fila):
	fila = get_object_or_404(Fila, pk=id_fila)
	sala = Sala.objects.all()
	id_sala = fila.sala
	filas = Fila.objects.filter(sala=id_sala)	
	sede = Sede.objects.all()
	id_sede = id_sala.sede
	salas = Sala.objects.filter(sede=id_sede)
	equipos_en_fila = Equipo.objects.filter(fila=fila)
	return render_to_response('ubicacion/lista_de_equipos_por_fila.html',{'sede':id_sede,'sala':id_sala,
		'salas':salas,'fila':fila,'equipos_en_fila':equipos_en_fila,'filas':filas},
	 context_instance=RequestContext(request))	


def listado_de_salas(request):
	salas = Sala.objects.all()
	filas = Fila.objects.all()
	equipos = Equipo.objects.all()
	rack = Rack.objects.all()
	return render_to_response('ubicacion/listado_de_salas.html'
		,{'filas':filas,'salas':salas,'equipos':equipos,'rack':rack
		}, context_instance=RequestContext(request))