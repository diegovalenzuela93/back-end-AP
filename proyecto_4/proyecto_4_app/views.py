from django.shortcuts import render
from proyecto_4_app.models import empleados 

# Create your views here.
def listaempleados(request):
    emplea = empleados.objects.all()
    data = {'emple' : emplea}
    
    return render(request, 'empleados.html', data)