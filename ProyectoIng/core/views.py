from django.shortcuts import render
from django.views.generic.base import TemplateView
from ad.models import Category
# Create your views here.



class sidebar(TemplateView):

    template_name = "core/busquedas-sidebar-filtros.html"

class no_sidebar(TemplateView):

    template_name = "core/template-no-sidebarhtml.html"

class base_barra(TemplateView):
    template_name = "core/base-barra.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.order_by('category_name')
        return context

class main_page(TemplateView):
    template_name= "core/blank.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.order_by('category_name')
        return context

