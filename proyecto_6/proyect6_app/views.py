from django.shortcuts import render, redirect
from . import forms
from proyect6_app.models import Proyecto

# Create your views here.
def registro(request):
    form = forms.registroProyecto()
    if(request.method == 'POST'):
        form = forms.registroProyecto(request.POST)
        if (form.is_valid()):
            form.save()
        return index(request)
    data = {'formss' : form}
    return render(request, 'registro.html', data)

def index(request):
    return render(request, 'index.html')

def listar(request):
    listado = Proyecto.objects.all()
    data = {'proyecto' : listado}
    
    return render(request, 'proyecto.html', data)

def elimminarProyecto(request, id):
    pro = Proyecto.objects.get(id=id)
    pro.delete()
    return redirect('/listado')

def modificarProyecto(request, id):
    pro = Proyecto.objects.get(id=id)
    form = forms.registroProyecto(instance=pro)
    if(request.method == 'POST'):
        form = forms.registroProyecto(request.POST)
        if (form.is_valid()):
            form.save()
        return index(request)
    
    data = {'formss' : form}
    return render(request, 'registro.html', data)
