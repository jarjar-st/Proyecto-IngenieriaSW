from django.db import models

# Create your models here.
class categories(models.Model):
    nombre = models.CharField(max_length=45)
    description = models.TextField()

    def __str__(self):
        return self.nombre