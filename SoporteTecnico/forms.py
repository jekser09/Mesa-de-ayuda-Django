from django import forms
from .models import Usuario,Area,Solicitud
from django.contrib.auth.forms import AuthenticationForm


class Login(AuthenticationForm):
    username=forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder':'Usuario','class':'campos'}),max_length=20)
    password=forms.CharField(label=False,widget=forms.PasswordInput(attrs={'placeholder':'Contraseña','class':'campos'}),max_length=20)
    iniSesion=forms.CharField(widget=forms.TextInput(attrs={'type':'submit','value':'Ingreso','class':'boton','id':'bIni'}))
    


class Registro(forms.ModelForm):
    passw1=forms.CharField(label=False,widget=forms.PasswordInput(attrs={'class':'componentes','id':'pass1','placeholder':'Digite una contraseña'}))
    passw2=forms.CharField(label=False,widget=forms.PasswordInput(attrs={'class':'componentes','id':'pass2','placeholder':'Repita la contraseña'}))
    registro=forms.CharField(label=False,widget=forms.TextInput(attrs={'class':'boton','id':'breg','type':'submit','value':'Registrarse','class':'boton','id':'bReg'}))

    class Meta:
        model=Usuario
        fields=('id','nombres','apellidos','email','username')
        labels={
            'id':False,
            'nombres':False,
            'apellidos':False,
            'email':False,
            'username':False
        }
        widgets={
            'id':forms.NumberInput(attrs={'class':'componentes','id':'identificacion','placeholder':'Id Asignado','required':'required'}),
            'nombres':forms.TextInput(attrs={'class':'componentes','id':'nom','placeholder':'Nombres'}),
            'apellidos':forms.TextInput(attrs={'class':'componentes','id':'ape','placeholder':'Apellidos'}),
            'email':forms.EmailInput(attrs={'class':'componentes','id':'ema','placeholder':'Correo Electronico'}),
            'username':forms.TextInput(attrs={'class':'componentes','id':'user','placeholder':'Digite un nombre de usuario'})
        }

class Solicitud(forms.ModelForm):
    nombreArea=Area.objects.all()
    class Meta:
        model=