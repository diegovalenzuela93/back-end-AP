from django.shortcuts import render
from proyecto_4_app.models import empleados 
from . import forms

# Create your views here.
def listaempleados(request):
    emplea = empleados.objects.all()
    data = {'emple' : emplea}
    
    return render(request, 'empleados.html', data)

def index(request):
    return render(request, 'index.html')

def registro(request):
    form = forms.registroEmpleados()
    data = {'formss' : form}
    return render(request, 'registro.html', data)