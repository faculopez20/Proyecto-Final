from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from Producto.models import Raqueta
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class Raqueta(ListView):
    model = Raqueta
    context_object_name = 'Raqueta'
    template_name = "Raqueta/Raqueta.html"
    
class CrearRaqueta(CreateView):
    model = Raqueta
    template_name = "Raqueta/crear_Raqueta.html"
    fields = ['marca', 'modelo', 'fecha_fabricacion', 'descripcion']
    success_url = reverse_lazy('Raqueta')

class EliminarRaqueta(LoginRequiredMixin, DeleteView):
    model = Raqueta
    template_name = "Raqueta/eliminar_Raqueta.html"
    success_url = reverse_lazy('Raqueta')

class EditarRaqueta(LoginRequiredMixin, UpdateView):
    model = Raqueta
    template_name = "Raqueta/editar_Raqueta.html"
    success_url = reverse_lazy('Raqueta')
    fields = ['marca', 'modelo', 'fecha_fabricacion', 'descripcion']

class DetalleRaqueta(DetailView):
    model = Raqueta
    template_name = "Raqueta/detalle_Raqueta.html"
# Create your views here.
