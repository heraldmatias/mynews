from django.views.generic import ListView, DetailView, TemplateView
from portada.models import Portada, PortadaBase
#from django.shortcuts import get_object_or_404
import datetime
from portada.forms import ResumenForm

class PortadaListView(ListView):
	model = Portada
	template_name = 'base.html'

	def get_queryset(self):
		return Portada.objects.filter(
			portada__fec_creacion=datetime.date.today()).select_related('diario')

	def get_context_data(self, **kwargs):
		ctx = super(PortadaListView, self).get_context_data(**kwargs)
		try:
			ctx['portada'] = PortadaBase.objects.get(fec_creacion=datetime.date.today())
		except:
			pass
		return ctx

class ProbarSudo(TemplateView):
	template_name = 'prueba.html'

	def post(self, request, *args, **kwargs):
		import os
		user = request.POST.get('user')
		admin = request.POST.get('admin')
		os.system('sudo ejabberdctl add-rosteritem %(user)s %(host)s %(admin)s %(host)s %(user)s admins both'
			% {'user':user,'admin':admin,'host':'localhost'} )
		os.system('sudo ejabberdctl add-rosteritem %(admin)s %(host)s %(user)s %(host)s %(admin)s users both'
			% {'user':user,'admin':admin,'host':'localhost'})
		return self.render_to_response(self.get_context_data())

class ResumirWebPage(TemplateView):
    template_name = 'resumen.html'
    
    def get_context_data(self, **kwargs):
        ctx = super(ResumirWebPage, self).get_context_data(**kwargs)
        ctx['form'] = ResumenForm()
        return ctx
    
    def post(self, request, *args, **kwargs):
        form = ResumenForm(request.POST.copy())
        if form.is_valid():
            form.summary()
        ctx = self.get_context_data()
        ctx['form'] = form
        return self.render_to_response(ctx)
            
            
