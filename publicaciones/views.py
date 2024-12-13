from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Post
# Create your views here.

class PaginaDeInicio(TemplateView):
    template_name = "inicio.html"
    
    
class PaginaDePublicaciones(ListView):
    template_name = "publicaciones.html"
    model = Post