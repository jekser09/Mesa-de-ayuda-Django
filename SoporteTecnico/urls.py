from django.urls import path
from . import views

urlpatterns=[
    path('',views.signin,name='signin'),
    path('registro/',views.registro,name='registro'),
    path('index/',views.baseMenu,name="baseMenu"),
    path('logout/',views.signout,name='signout'),
    path('soporte/',views.soporte,name='soporte'),
    path('solicitudes/',views.solicitudes,name='solicitudes')
]