from django.db import models

# Create your models here.
class Movie(models.Model):
    id=models.CharField(primary_key=True,max_length=20)
    nombre= models.CharField(max_length=50)
    pais= models.CharField(max_length=30)
    calificacion= models.DecimalField(max_digits=2,decimal_places=1)
     
    def __str__(self) -> str:
        return self.nombre
