from django.db import models
from account.models import Account
from ad.models import Ad
from store.models import Store

# Create your models here.
class Image(models.Model):
    img_route= models.ImageField(upload_to="Images", verbose_name="Ruta de la Imagen")

    class Meta():
        verbose_name= "Imagen"
        verbose_name_plural= "Imagenes"

class ImageXUser(models.Model):
    img= models.ForeignKey(Image, related_name="user_img", on_delete= models.CASCADE, null=False, blank=False, verbose_name="Ruta de la Imagen")
    user= models.ForeignKey(Account, related_name="img_user_owner", on_delete= models.CASCADE, null=False, blank=False, verbose_name="Usuario al que pertenece la imagen")

    class Meta():
        verbose_name= "Imagen por Usuario"
        verbose_name_plural= "Imagenes por Usuario"

class ImageXAd(models.Model):
    img= models.ForeignKey(Image, related_name="ad_img", on_delete= models.CASCADE, null=False, blank=False, verbose_name="Ruta de la Imagen")
    ad= models.ForeignKey(Ad, related_name="img_ad_owner", on_delete= models.CASCADE, null=False, blank=False, verbose_name="Publicacion a la que pertenece la imagen")

    class Meta():
        verbose_name= "Imagen por Anuncio"
        verbose_name_plural= "Imagenes por Anuncio"

class ImageXStore(models.Model):
    img= models.ForeignKey(Image, related_name="store_img", on_delete= models.CASCADE, null=False, blank=False, verbose_name="Ruta de la Imagen")
    store= models.ForeignKey(Store, related_name="img_store_owner", on_delete= models.CASCADE, null=False, blank=False, verbose_name="Tienda a la que pertenece la imagen")

    class Meta():
        verbose_name= "Imagen por Tienda"
        verbose_name_plural= "Imagenes por Tienda"

