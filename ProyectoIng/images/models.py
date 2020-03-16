from django.db import models
from account.models import Account

# Create your models here.
"""Clase imagenes:
Atributo: [Direccion de la imagen]"""
class Image(models.Model):
    img_route= models.ImageField(upload_to="Images", verbose_name="Ruta de la Imagen")

    class Meta():
        verbose_name= "Imagen"
        verbose_name_plural= "Imagenes"

"""Clase Imagenes X Usuario
Atributo: [ID imagen, ID usuario]"""
class ImageXUser(models.Model):
    img= models.ForeignKey(Image, related_name="user_img", on_delete= models.CASCADE, null=False, blank=False, verbose_name="Ruta de la Imagen")
    user= models.ForeignKey(Account, related_name="img_user_owner", on_delete= models.CASCADE, null=False, blank=False, verbose_name="Usuario al que pertenece imagen")

    class Meta():
        verbose_name= "Imagen por Usuario"
        verbose_name_plural= "Imagenes por Usuario"





