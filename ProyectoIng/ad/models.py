from django.db import models
from account.models import Account
from store.models import Store

# Create your models here.
class Categories(models.Model):
    categori_name=models.CharField(max_length=100,blank=False,null=False)
    categori_description= models.TextField(null=False, blank=False)

    def __str__(self):
        return self.categori_name

class Ad_Kind(models.Model):
    ad_kind= models.CharField(max_length=20)

    def __str__(self):
        return self.ad_kind

class Ubication(models.Model):
    direction = models.CharField(primary_key=True, max_length=50, default="Ninguna")
    correlative_direction= models.ForeignKey("self",on_delete=models.CASCADE, default="Ninguna", blank=True, null=True)

    def __str__(self):
        return self.direction

class Uniti(models.Model):
    uniti_tipe= models.CharField(max_length=10, default="Unidad")

    def __str__(self):
        return self.uniti_tipe

class Ad(models.Model):
    id_user = models.ForeignKey(Account, on_delete=models.CASCADE)
    id_store = models.ForeignKey(Store, on_delete= models.CASCADE)
    id_ubication= models.ForeignKey(Ubication, on_delete= models.CASCADE)
    id_ad_kind= models.ForeignKey(Ad_Kind, on_delete= models.CASCADE)
    id_categori= models.ForeignKey(Categories, on_delete= models.CASCADE)
    id_uniti= models.ForeignKey(Uniti, on_delete= models.CASCADE)
    ad_name= models.CharField(max_length=100)
    ad_description= models.TextField()
    price= models.FloatField()

    def __str__(self):
        return self.ad_name
