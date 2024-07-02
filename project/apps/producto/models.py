from django.db import models
from django.utils import timezone

class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=100, null=True, blank=True, verbose_name="Descripción")

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Categoría de producto"
        verbose_name_plural = "Categorías de Productos"


class Producto(models.Model):
    """Productos que corresponden a una categoria"""
    categoria = models.ForeignKey(ProductoCategoria, on_delete=models.SET_NULL, blank=True, null=True)
    nombre = models.CharField(max_length=150)
    unidad_de_medida = models.CharField(max_length=150)
    cantidad = models.FloatField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=250, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(default=timezone.now, editable=False, verbose_name="Fecha de actualización")

