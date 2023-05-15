from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='signup'),
    path('registro/',views.registro,name='registro'),
    path('general/',views.vistaGen,name="general")
]