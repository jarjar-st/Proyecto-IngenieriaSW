from django.db import models
from location.models import Location
# Create your models here.
class Store(models.Model):
    store_name= models.CharField(max_length=100,null=False,blank=False)
    store_description= models.TextField(null=False,blank=False)
    store_location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.store_name