from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self,id,nombres,apellidos,email,username,password=None):
        if not email:
            raise ValueError('El usuario deber contener un correo')
        usuario=self.model(id=id,
                           nombres=nombres,
                           apellidos=apellidos,
                           email=self.normalize_email(email),
                           username=username)
        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self,id,nombres,apellidos,email,username,password):
        usuario=self.create_user(id=id,
                                 nombres=nombres,
                                 apellidos=apellidos,
                                 email=email,
                                 username=username,
                                 password=password)
        usuario.usuario_admin=True
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser):
    id=models.IntegerField(primary_key=True,unique=True,null=False,blank=False)
    nombres=models.CharField(max_length=80,blank=False)
    apellidos=models.CharField(max_length=80,blank=False)
    email=models.EmailField(unique=True,null=False,blank=False)
    username=models.CharField(unique=True ,max_length=100,null=False,blank=False)
    usuario_activo=models.BooleanField(default=True)
    usuario_admin=models.BooleanField(default=False)
    objects=UsuarioManager()
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['id','nombres','apellidos','email']

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_admin

    def __str__(self) -> str:
        return f'{self.nombres} {self.apellidos}'

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

class Solicitud(models.Model):
    codigo=models.AutoField
    idarea=models.ForeignKey(Area,blank=False,null=False)
