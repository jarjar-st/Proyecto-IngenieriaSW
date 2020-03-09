from django.db import models

# Create your models here.
class product(models.Model):
    nombre= models.CharField(max_length=20)
    description= models.TextField()
    precio= models.BigIntegerField()
    #imagen = models.ImageField (upload_to="products")

    def __str__(self):
        return self.nombre
