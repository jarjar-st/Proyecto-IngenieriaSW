from django.db import models

# Create your models here.
class Store(models.Model):
    store_name= models.CharField(max_length=100,null=False,blank=False)
    store_description= models.TextField(null=False,blank=False)

    def __str__(self):
        return self.store_name