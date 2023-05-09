from django import forms

class Login(forms.Form):
    user=forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder':'Usuario','class':'campos ali'}),max_length=20)
    password=forms.CharField(label=False,widget=forms.PasswordInput(attrs={'placeholder':'Contraseña','class':'campos ali'}),max_length=20)
    iniSesion=forms.CharField(widget=forms.TextInput(attrs={'type':'submit','value':'Iniciar Sesion','class':'boton ali','id':'bIni'}))
    registro=forms.CharField(widget=forms.TextInput(attrs={'type':'submit','value':'Registrarse','class':'boton ali','id':'bReg'}))