from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import Registro,Login,FormSolicitud
from .models import Usuario,Area,Solicitud

# Create your views here.
def signin(request):
    if request.method=='GET':
        return render(request,'Signin.html',{
            'form':Login()
        })
    elif request.method=='POST':
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'Signin.html',{
            'form':Login(),
            'error':'Usuario o contraseña incorrectos'
            })
        else:
            login(request,user)
            return redirect('baseMenu')

def registro(request):
    if request.method=='GET':
        return render(request,'Registro.html',{
            'form':Registro()
        })
    elif request.method=='POST':
        try:
            if request.POST['passw1']==request.POST['passw2']:
                user=Usuario.objects.create_user(id=request.POST['id'],
                                            nombres=request.POST['nombres'],
                                            apellidos=request.POST['apellidos'],
                                            email=request.POST['email'],
                                            username=request.POST['username'],
                                            password=request.POST['passw1'])
                login(request,user)
                return redirect('baseMenu')
            else:
                return render(request,'Registro.html',{'form':Registro(),'error':'Las contraseñas no coinciden'})
        except Exception as e:
            return render(request,'Registro.html',{
            'form':Registro(),
            'error':f'Ocurrio un error: {e}'
        })

def signout(request):
    logout(request)
    return redirect('signin')

@login_required
def baseMenu(request):
    return render(request,'baseMenu.html',{'user':request.user})

@login_required
def soporte(request):
    form=FormSolicitud
    try:
        if request.method=='GET':
            return render(request,'menuSoporte.html',{'form':form})
        elif request.method=='POST':
            a=Area.objects.get(nombre=request.POST['areas'])
            Solicitud(idarea=a,nombrearea=a.nombre,
                      idpersona=request.user,nombrepersona=request.user.nombres,
                      descripcion=request.POST['descripcion']).save()
            return render(request,'menuSoporte.html',{'form':form})
    except Exception as e:
        return render(request,'menuSoporte.html',{'form':form,'error':f'Error al guardar solicitud ({e})'})

@login_required
def solicitudes(request):
    def aux(soli:Solicitud):
            return FormSolicitud(instance=soli)
    formularios=list(map(aux,Solicitud.objects.all()))
    if request.method=='GET':return render(request,'solicitudes.html',{'forms':formularios})
    elif request.method=='POST':
        print(request.POST)
        return redirect("solicitudes")
