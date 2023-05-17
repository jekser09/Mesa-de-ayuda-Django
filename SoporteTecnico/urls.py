from django.urls import path
from . import views

urlpatterns=[
    path('',views.signin,name='signup'),
    path('registro/',views.registro,name='registro'),
    path('index/',views.baseMenu,name="baseMenu")
]