from django.shortcuts import render
from django.views.generic import CreateView
from apps.interfaz.models import Interfaz

class RegistrarInterfaz(CreateView):
	template_name = 'interfaz/registrarInterfaz.html'
	model = Interfaz

