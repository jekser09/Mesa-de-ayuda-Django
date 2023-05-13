from django import forms
from django.contrib.auth.forms import UserCreationForm
class Login(forms.Form):
    user=forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder':'Usuario','class':'campos'}),max_length=20)
    password=forms.CharField(label=False,widget=forms.PasswordInput(attrs={'placeholder':'Contraseña','class':'campos'}),max_length=20)
    iniSesion=forms.CharField(widget=forms.TextInput(attrs={'type':'submit','value':'Ingreso','class':'boton','id':'bIni'}))
    registro=forms.CharField(widget=forms.TextInput(attrs={'type':'submit','value':'Registro','class':'boton','id':'bReg'}))

class Registro(forms.Form):
    documento=forms.IntegerField(label=False,widget=forms.NumberInput(attrs={'placeholder':'Documento'}))
    nombres=forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder':'Nombres'}))
    apellidos=forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder':'Apellidos'}))
    area=forms.ChoiceField(label=False,widget=forms.Select,choices=(('Zona T','Luna'),('Usaquen','Amarti')))
    email=forms.EmailField(label=False,widget=forms.EmailInput(attrs={'placeholder':'Correo Electronico'}))
    usuario=forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder':'Digite un nombre de usuario'}))
    passw1=forms.CharField(label=False,widget=forms.PasswordInput(attrs={'placeholder':'Digite una contraseña'}))
    passw2=forms.CharField(label=False,widget=forms.PasswordInput(attrs={'placeholder':'Repita la contraseña'}))