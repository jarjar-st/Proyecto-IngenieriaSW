from django.contrib import admin
from .models import UserImage, AdImg, ImagesXUser, ImageXAd

# Register your models here.
admin.site.register(UserImage)
admin.site.register(AdImg)
admin.site.register(ImagesXUser)
admin.site.register(ImageXAd)