from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .models import Usuario

from .forms import Login,Registro
# Create your views here.
def index(request):
    if request.method=='GET':
        return render(request,'Signup.html',{
            'form':Login()
        })
    else:
        try:
            if Usuario.objects.get(usuario=request.POST['user']) and Usuario.objects.get(contraseña=request.POST['password']):
                return redirect('general')
        except Exception:
            messages.success(request, 'No existe')
            return render(request,'Signup.html',{
            'form':Login()
            })

def registro(request):
    if request.method=='GET':
        return render(request,'Registro.html',{
            'form':Registro()
        })
    

def vistaGen(request):
    return HttpResponse('<h1>General</h1>')
