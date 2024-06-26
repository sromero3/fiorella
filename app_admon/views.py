from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app_admon.models import *
from app_admon.forms import *

def Index(request):
    return render(request, 'app_admon/index.html')

@login_required
def inicioView(request):
    xAcceso = "Administrador"
    xUsuario = request.user
    context = {
        'xUsuario': request.user,
        }
    return render(request, 'app_admon/inicio.html', context)


@login_required
def clientesView(request):
    xUsuario = request.user

    xClientes = Cliente.objects.values('id','ced_rif','nombre','telefono','instagram','nacimiento','status__status').filter(status=2)
    
    context = {
        'xUsuario': xUsuario,
        'xClientes': xClientes
    }
    return render(request, 'app_admon/clientes.html', context)

@login_required
def add_clienteView(request):
    xUsuario = request.user
    #xCondominios = xUsuario.profile.condominios.all()

    xOpcion = "Agregando"
    xPrefijos_ced_rif = Prefijo_ced_rif.objects.all()
    xPrefijos = Prefijo_telefono.objects.all()
       
    form = Agregar_clienteForm()

    if request.method == 'POST':
        form = Agregar_clienteForm(request.POST)

        #for field in form:
        #   print("Field:", field.name, "-> ", field.errors)

        #print("------------------------ POST ---------------------")
        #print(request.POST)
        #print("------------------------ POST ---------------------")
            
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.ced_rif = request.POST.get('prefijo_r') + request.POST.get('ced_rif')
            cliente.telefono = request.POST.get('prefijo') + request.POST.get('telefono')
            cliente.save()
            return redirect('clientes')
        else:
            messages.error(
                request, "Su operación no se puedo efectuar debido a problemas en el Servidor. El formulario no es válido")
    
    context = {
     'form': form,
        'xOpcion': xOpcion,
        
        'xPrefijos_ced_rif':xPrefijos_ced_rif,
        'xPrefijos':xPrefijos,
       
    }
    return render(request, 'app_admon/cliente_crud.html', context)

@login_required
def colaboradorasView(request):
    xUsuario = request.user

    xColaboradoras = Colaborador.objects.values('id','ced_rif','nombre','telefono','instagram','nacimiento','status__status').filter(status=2)
    
    context = {
        'xUsuario': xUsuario,
        'xColaboradoras': xColaboradoras
    }
    return render(request, 'app_admon/colaboradoras.html', context)

