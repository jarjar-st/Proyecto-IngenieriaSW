from django.db import models
from account.models import Account
from store.models import Store

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=100,blank=False,null=False)
    category_description= models.TextField(null=False, blank=False)

    def __str__(self):
        return self.category_name
    
    class Meta():
        verbose_name= "Categoría"
        verbose_name_plural= "Categorías"

class AdKind(models.Model):
    ad_kind= models.CharField(max_length=20)

    def __str__(self):
        return self.ad_kind
    
    class Meta():
        verbose_name= "Tipo de Anuncio"
        verbose_name_plural= "Tipos de Anuncio"

class Location(models.Model):
    direction = models.CharField(primary_key=True, max_length=50, default="Ninguna")
    correlative_direction= models.ForeignKey("self",on_delete=models.CASCADE, default="Ninguna", blank=True, null=True)

    def __str__(self):
        return self.direction
    
    class Meta():
        verbose_name= "Ubicación"
        verbose_name_plural= "Ubicaciones"

class Unit(models.Model):
    unit_type= models.CharField(max_length=10, default="Unidad")

    def __str__(self):
        return self.unit_type
    
    class Meta():
        verbose_name= "Unidad"
        verbose_name_plural= "Unidades"

class Ad(models.Model):
    id_user = models.ForeignKey(Account, on_delete=models.CASCADE)
    id_store = models.ForeignKey(Store, on_delete= models.CASCADE,default=None, blank=True, null=True)
    id_location= models.ForeignKey(Location, on_delete= models.CASCADE)
    id_ad_kind= models.ForeignKey(AdKind, on_delete= models.CASCADE)
    id_category= models.ForeignKey(Category, on_delete= models.CASCADE)
    id_unit= models.ForeignKey(Unit, on_delete= models.CASCADE, default = None, blank=True, null=True)
    ad_name= models.CharField(max_length=100)
    ad_description= models.TextField()
    price= models.FloatField()

    def __str__(self):
        return self.ad_name

    class Meta():
        verbose_name= "Anuncio"
        verbose_name_plural= "Anuncios"
