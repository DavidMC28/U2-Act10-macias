

# Create your models here.
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # ← Campo agregado
    descripcion = models.TextField(blank=True, null=True)
    existencias = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre