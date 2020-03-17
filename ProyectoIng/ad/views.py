from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Ad
from account.models import Account
from images.models import Image

class ShowAdsListView(ListView):

    model= Ad
    template_name="ad_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["ads_data"]= Ad.objects.prefetch_related()
        
        return context
#id_user ,id_store ,id_location,id_ad_kind,id_category,id_unit,ad_name,ad_description,price,date_created

class AdCreate(CreateView):
    model = Ad
    fields = ['ad_name', 'ad_description', 'price', 'ad_images']

   