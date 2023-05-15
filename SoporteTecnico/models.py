from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.
class Sede(models.Model):
    idsede=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100,null=False,blank=False)
    pais=models.CharField(max_length=100,null=False,blank=False)
    direccion=models.TextField(blank=False,null=False)

    def __str__(self) -> str:
        return self.nombre

class Area(models.Model):
    idarea=models.AutoField(primary_key=True)
    idsede=models.ForeignKey(Sede,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=100,null=False,blank=False)
    def __str__(self) -> str:
        return self.nombre

class Usuario(models.Model):
    documento=models.IntegerField(primary_key=True,unique=True,null=False,blank=False)
    tipodocumento=models.CharField(max_length=50,blank=False,null=False)
    nombre=models.CharField(max_length=80,null=False,blank=False)
    apellidos=models.CharField(max_length=80,null=False,blank=False)
    idarea=models.ForeignKey(Area,on_delete=models.CASCADE)
    area=models.CharField(max_length=100,null=False,blank=False)
    email=models.EmailField(unique=True,null=False,blank=False)
    usuario=models.CharField(max_length=100,null=False,blank=False)
    contraseña=models.CharField(max_length=100,blank=False,null=False)
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellidos}'
