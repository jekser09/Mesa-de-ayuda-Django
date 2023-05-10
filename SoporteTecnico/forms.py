from django import forms

class Login(forms.Form):
    user=forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder':'Usuario','class':'campos ali'}),max_length=20)
    password=forms.CharField(label=False,widget=forms.PasswordInput(attrs={'placeholder':'Contraseña','class':'campos'}),max_length=20)
    iniSesion=forms.CharField(widget=forms.TextInput(attrs={'type':'submit','value':'Ingreso','class':'boton','id':'bIni'}))
    registro=forms.CharField(widget=forms.TextInput(attrs={'type':'submit','value':'Registro','class':'boton ali','id':'bReg'}))

class Registro(forms.Form):
    nombres=forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder':'Nombres'}))
    apellidos=forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder':'Apellidos'}))
    area=forms.ChoiceField(label=False,widget=forms.Select,choices=(('Zona T','Luna'),('Usaquen','Amarti')))
    id=forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder':'Cargo'}))
    numCon=forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder':'Numero'}))
    usuario=forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder':'Usuario','class':'campos'}),max_length=20)
    password=forms.CharField(label=False,widget=forms.PasswordInput(attrs={'placeholder':'Contraseña','class':'campos'}),max_length=20)