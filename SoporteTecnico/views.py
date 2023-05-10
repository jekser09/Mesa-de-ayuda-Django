from django.shortcuts import render
from .forms import Login,Registro
# Create your views here.
def index(request):
    return render(request,'index.html',{
        'form':Login()
    })

def registro(request):
    return render(request,'Registro.html',{
        'form':Registro()
    })