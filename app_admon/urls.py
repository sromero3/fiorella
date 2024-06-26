from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from app_admon.forms import LoginForm

urlpatterns = [
    path('', views.Index, name="index"),

    path('accounts/login/', auth_views.LoginView.as_view(
       authentication_form=LoginForm,
       ), name="login"),

    path('inicio/', views.inicioView, name='inicio'),
    
    path('clientes/', views.clientesView, name='clientes'),
    path('add_cliente/', views.add_clienteView, name='add_cliente'),
    
    path('colaboradoras/', views.colaboradorasView, name='colaboradoras'),
]