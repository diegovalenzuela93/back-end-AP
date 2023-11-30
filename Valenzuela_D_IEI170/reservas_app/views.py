from django.shortcuts import redirect, render
from . import forms
from .models import Reservas

# Create your views here.
def index(request):
    return render(request, 'index.html')

def verReservas(request):
    reservas = Reservas.objects.all()
    data = {'reservas': reservas}
    return render(request, 'reservas.html', data)

def formularioReserva(request):
    form = forms.FormularioReserva()
    if(request.method == 'POST'):
        form = forms.FormularioReserva(request.POST)
        if(form.is_valid()):
            form.save()
            return verReservas(request)
    data = {'form' : form}
    return render(request, 'formulario.html', data)

def eliminarReserva(request, id):
    eliminar = Reservas.objects.get(id=id)
    eliminar.delete()
    return redirect('/reservas/')

def actualizarReserva(request, id):
    reserva = Reservas.objects.get(id=id)
    if(request.method == 'POST'):
        form = forms.FormularioReserva(request.POST, instance=reserva)
        if (form.is_valid()):
            form.save()
            return redirect('/reservas/')
    else:
        form = forms.FormularioReserva(instance=reserva)
    
    data = {'form' : form}
    return render(request, 'formulario.html', data)
