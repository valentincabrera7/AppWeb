from django.db import models
#! LOS MODELOS SON CLASES 

class Pais(models.Model): #! BASE DE DATOS DESPUES DE MIGRAR 
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre #! PARA QUE ME DIGA EL NOMBRE EN EL PANEL DE ADMIN DE DJANGO
    
class Cliente(models.Model): #! BASE DE DATOS DESPUES DE MIGRAR CON COMANDOS
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField()
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True) 

    def __str__(self):
        return f"{self.apellido} {self.nombre}" #! PARA QUE ME DIGA EL NOMBRE y APELLIDO EN EL PANEL DE ADMIN DE DJANGO