from django.shortcuts import render, redirect, get_object_or_404

from core.models import Agendar, Servicio
from .forms import AgendarForm, ServicioForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'core/home.html')


def agendar(request):
    data = {    
        'form' : AgendarForm()
    }
    
    if request.method == 'POST':
        formulario = AgendarForm(data=request.POST)
        if formulario.is_valid:
            formulario.save()
            data["alerta"] = "Hora Agendada"
        else:
            data['form'] = formulario

    return render(request, 'core/agendar.html', data)

def agregar_servicio(request):
    data = {
        'form' : ServicioForm()
    }

    if request.method == 'POST':
        formulario = ServicioForm(data=request.POST)
        if formulario.is_valid:
            formulario.save()
            data["alerta"] = "Servicio agregado"
        else:
            data['form'] = formulario


    return render(request, 'core/servicios/agregar.html', data)

def listar_servicio(request):
    servicios = Servicio.objects.all()

    data = {
        'servicios': servicios
    }

    return render(request, 'core/servicios/listar.html', data)

def editar_servicio(request, id):

    servicio = get_object_or_404(Servicio, id=id)

    data = {
        'form': ServicioForm(instance=servicio)
    }

    if request.method == 'POST':
        formulario = ServicioForm(data=request.POST, instance=servicio)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listar_servicio')
        data["form"] = formulario

    return render(request, 'core/servicios/editar.html', data)

def eliminar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    servicio.delete()
    return redirect(to='listar_servicio')

def registro(request):
    data = {
        'form' : CustomUserCreationForm
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/signup.html', data)

def listar_hora(request):
    horas = Agendar.objects.all()

    data = {
        'horas': horas
    }

    return render(request, 'core/horas/listar.html', data)

def listar_usuario(request):
    usuarios = User.objects.all()

    data = {
        'usuarios': usuarios
    }

    return render(request, 'core/usuarios/listar.html', data)