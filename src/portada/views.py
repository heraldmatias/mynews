from django.views.generic import ListView, DetailView
from .models import Portada, PortadaBase
from django.shortcuts import get_object_or_404
import datetime

class PortadaListView(ListView):
	model = Portada
	template_name = 'base.html'

	def get_queryset(self):
		return Portada.objects.filter(
			portada__fec_creacion=datetime.date.today()).select_related('diario')

	def get_context_data(self, **kwargs):
		ctx = super(PortadaListView, self).get_context_data(**kwargs)
		ctx['portada'] = get_object_or_404(PortadaBase,fec_creacion=datetime.date.today())
		return ctx