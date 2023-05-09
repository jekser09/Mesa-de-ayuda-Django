from django.shortcuts import render
from .forms import Login
# Create your views here.
def index(request):
    return render(request,'Index.html',{
        'form':Login()
    })