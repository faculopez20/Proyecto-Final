from django.db import models



class Raqueta(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=30)
    año_de_fabricacion = models.IntegerField()
    
    def __str__(self):
        return f"{self.marca} {self.modelo}" 