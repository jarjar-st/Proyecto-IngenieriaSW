from django.db import models

# Create your models here.
class service(models.Model):
    nombre= models.CharField(max_length=20)
    desription= models.TextField()
    precio= models.BigIntegerField()

    def __str__(self):
        return self.nombre
