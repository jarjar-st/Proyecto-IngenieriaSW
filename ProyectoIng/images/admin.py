from django.contrib import admin
from .models import Image, ImageXUser, ImageXAd, ImageXStore

# Register your models here.
admin.site.register(Image)
admin.site.register(ImageXStore)
admin.site.register(ImageXUser)
admin.site.register(ImageXAd)