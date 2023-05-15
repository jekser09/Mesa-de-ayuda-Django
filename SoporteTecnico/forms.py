from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

class Login(forms.Form):
    user=forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder':'Usuario','class':'campos'}),max_length=20)
    password=forms.CharField(label=False,widget=forms.PasswordInput(attrs={'placeholder':'Contraseña','class':'campos'}),max_length=20)
    iniSesion=forms.CharField(widget=forms.TextInput(attrs={'type':'submit','value':'Ingreso','class':'boton','id':'bIni'}))

class Registro(forms.Form):
    tipodocumento=forms.ChoiceField(widget=forms.Select(attrs={'class':'componentes','id':'tdoc'}),choices=[('none','Tipo Documento')])
    documento=forms.IntegerField(label=False,widget=forms.NumberInput(attrs={'class':'componentes','id':'doc','placeholder':'Documento'}))
    nombres=forms.CharField(label=False,widget=forms.TextInput(attrs={'class':'componentes','id':'nom','placeholder':'Nombres'}))
    apellidos=forms.CharField(label=False,widget=forms.TextInput(attrs={'class':'componentes','id':'ape','placeholder':'Apellidos'}))
    sede=forms.ChoiceField(label=False,widget=forms.Select(attrs={'class':'componentes','id':'sede'}),choices=[('none','Seleccionar Sede')])
    area=forms.ChoiceField(label=False,widget=forms.Select(attrs={'class':'componentes','id':'area'}),choices=[('none','Selecionar Area')])
    email=forms.EmailField(label=False,widget=forms.EmailInput(attrs={'class':'componentes','id':'ema','placeholder':'Correo Electronico'}))
    usuario=forms.CharField(label=False,widget=forms.TextInput(attrs={'class':'componentes','id':'user','placeholder':'Digite un nombre de usuario'}))
    passw1=forms.CharField(label=False,widget=forms.PasswordInput(attrs={'class':'componentes','id':'pass1','placeholder':'Digite una contraseña'}))
    passw2=forms.CharField(label=False,widget=forms.PasswordInput(attrs={'class':'componentes','id':'pass2','placeholder':'Repita la contraseña'}))
    registro=forms.CharField(label=False,widget=forms.TextInput(attrs={'class':'boton','id':'breg','type':'submit','value':'Registrarse','class':'boton','id':'bReg'}))