from django.db import models
#! LOS MODELOS SON CLASES 

class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField()
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True) 
