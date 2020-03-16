from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Ad
from account.models import Account
from images.models import ImageXAd
from images.models import Image

class ShowAdsListView(ListView):

    model = Ad
    template_name="ad_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['adinfo'] = Ad.objects.all()
        #context['images'] = Image.objects.select_related()
        
        
    
        return context
#id_user ,id_store ,id_location,id_ad_kind,id_category,id_unit,ad_name,ad_description,price,date_created

    