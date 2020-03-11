from django.db import models
from account.models import Account
from ad.models import Ad

# Create your models here.
class UserImage(models.Model):
    img_route= models.ImageField(upload_to="User_Images", verbose_name="Ruta de la Imagen")

    class Meta():
        verbose_name= "Imagen de Usuario"
        verbose_name_plural= "Imagen de Usuarios"

class ImagesXUser(models.Model):
    user_img= models.ForeignKey(UserImage, related_name="user_img", on_delete= models.CASCADE, null=False, blank=False, verbose_name="Ruta de la Imagen")
    img_user_owner= models.ForeignKey(Account, related_name="img_user_owner", on_delete= models.CASCADE, null=False, blank=False, verbose_name="Usuario al que pertenece la imagen")

    class Meta():
        verbose_name= "Imagen por usuario"
        verbose_name_plural= "Imagenes por Usuario"

class AdImg(models.Model):
    img_route= models.ImageField(upload_to="Ad_Images", verbose_name="Ruta de la Imagen")

    class Meta():
        verbose_name= "Imagen de Anuncio"
        verbose_name_plural= "Imagen de Anuncios"

class ImageXAd(models.Model):
    ad_img= models.ForeignKey(AdImg, related_name="ad_img", on_delete= models.CASCADE, null=False, blank=False, verbose_name="Ruta de la Imagen")
    img_ad_owner= models.ForeignKey(Ad, related_name="img_ad_owner", on_delete= models.CASCADE, null=False, blank=False, verbose_name="Publicacion a la que pertenece la imagen")

    class Meta():
        verbose_name= "Imagen por anuncio"
        verbose_name_plural= "Imagenes por Anuncio"



