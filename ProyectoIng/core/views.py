from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class reg(TemplateView):

    template_name = "core/simple.html"

class sidebar(TemplateView):

    template_name = "core/busquedas-sidebar-filtros.html"

class no_sidebar(TemplateView):

    template_name = "core/template-no-sidebarhtml.html"

class base_barra(TemplateView):

    template_name = "core/base-barra.html"


