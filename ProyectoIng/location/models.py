from django.db import models

# Create your models here.
class Location(models.Model):
    direction = models.CharField(primary_key=True, max_length=50, default="Ninguna")
    correlative_direction= models.ForeignKey("self",on_delete=models.CASCADE, default="Ninguna", blank=True, null=True)

    def __str__(self):
        return self.direction
    
    class Meta():
        verbose_name= "Ubicación"
        verbose_name_plural= "Ubicaciones"