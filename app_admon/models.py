from django.db import models

# Create your models here.
class C_status(models.Model):
    status = models.CharField(max_length=10)

class Cliente(models.Model):
    ced_rif = models.CharField(max_length=10)
    nombre = models.CharField(max_length=40)
    telefono = models.CharField(max_length=11)
    direccion = models.TextField(max_length=200)
    instagram = models.CharField(max_length=40)
    nacimiento = models.DateField(null=True)
    creado = models.DateTimeField(auto_now_add=True, null=False)
    status = models.ForeignKey(C_status, on_delete=models.CASCADE, default=2)
    
    # que valor va a retornar al llamar el objeto
    def __str__(self) -> str:
        return self.nombre

class Prefijo_telefono(models.Model):
    prefijo_t = models.CharField(max_length=4)

    def __str__(self):
        return self.prefijo_t
    
class Prefijo_ced_rif(models.Model):
    prefijo_r = models.CharField(max_length=1)

    def __str__(self):
        return self.prefijo_r    
 
class Servicio(models.Model):
    especialidad = models.CharField(max_length=4)

    def __str__(self):
        return self.especialidad



class Colaborador(models.Model):
    ced_rif = models.CharField(max_length=10)
    nombre = models.CharField(max_length=40)
    telefono = models.CharField(max_length=11)
    direccion = models.TextField(max_length=200)
    instagram = models.CharField(max_length=40)
    nacimiento = models.DateField(null=True)
    creado = models.DateTimeField(auto_now_add=True, null=False)
    status = models.ForeignKey(C_status, on_delete=models.CASCADE, default=2)
    Servicio = models.ManyToManyField(Servicio)

    
    # que valor va a retornar al llamar el objeto
    def __str__(self) -> str:
        return self.nombre