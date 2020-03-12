from django.db import models
from account.models import Account
from store.models import Store

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=100,blank=False,null=False)
    category_description= models.TextField(null=False, blank=False)
    category_icon_class= models.CharField(max_length=100,null=False, blank=False)

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
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ad_name

    class Meta():
        verbose_name= "Anuncio"
        verbose_name_plural= "Anuncios"

class Currency(models.Model):
    currency_name= models.CharField(max_length=100,blank=False,null=False)
    currency_sign = models.CharField(max_length=5,blank=False,null=False)

    def __str__(self):
        return self.currency_name

    class Meta():
        verbose_name= "Moneda"
        verbose_name_plural= "Monedas"

class PriceRange(models.Model):
    min_price = models.FloatField(blank=False,null=False)
    max_price = models.FloatField(blank=False,null=False)
    currency = models.ForeignKey(Currency, on_delete= models.CASCADE)

    def __str__(self):
        return self.currency.currency_sign+self.min_price+'-'+self.max_price

    class Meta():
        verbose_name= "Rango de Precio"
        verbose_name_plural= "Rangos de Precio"

class CurrencyConversion(models.Model):
    currency_one = models.ForeignKey(Currency,related_name="currency_one", on_delete= models.CASCADE)
    currency_two = models.ForeignKey(Currency,related_name="currency_two", on_delete= models.CASCADE)
    one_equals = models.FloatField(blank=False,null=False)

    def __str__(self):
        return self.currency_one.currency_sign+'1='+self.currency_two.currency_sign+str(self.one_equals)

    class Meta():
        verbose_name= "Conversión de Moneda"
        verbose_name_plural= "Conversiones de Moneda"
