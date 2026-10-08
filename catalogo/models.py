from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    # Campo para la foto (permite que quede en blanco inicialmente)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"