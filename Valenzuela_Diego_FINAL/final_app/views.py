from django.http import JsonResponse
from django.shortcuts import redirect, render
from final_app import forms
from final_app import models
from .serializer import InstitucionesSerializer, InscritosSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404


# Create your views here.
def index(request):
    return render(request, 'index.html')

def inscripciones(request):
    formulario = forms.formInscripciones()
    if request.method == 'POST':
        formulario = forms.formInscripciones(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/')
    data = {'form': formulario}
    return render(request, 'inscripcion.html', data)

def instituciones(request):
    formulario = forms.formInstituciones()
    if request.method == 'POST':
        formulario = forms.formInstituciones(request.POST)
        if formulario.is_valid():
            formulario.save()
        return redirect('/')
    data = {'form': formulario}
    return render(request, 'institucion.html', data)


def estudiante(request):
    data = {
        'id' : 1,
        'Nombre' : 'Diego Valenzuela',
        'Carrera' : 'Analista Programador',
        'Email' : 'diego.valenzuela75@inacapmail.cl'
    }
    return JsonResponse(data)


# Function Based Views
@api_view(['GET'])
def api(request):
    if request.method == 'GET':
        insti = models.instituciones.objects.all()
        serializer = InstitucionesSerializer(insti, many=True)
        return Response(serializer.data)


# Class Based Views
class Inscritos_List_class(APIView):
    def get(self, request):
        inscritos = models.inscritos.objects.all()
        serial = InscritosSerializer(inscritos, many=True)
        return Response(serial.data)
    
    def post(self,request):
        serial = InscritosSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Inscritos_detalle_class(APIView):
    def get_object(self, id):
        try:
            return models.inscritos.objects.get(pk=id)
        except models.inscritos.DoesNotExist:
            return Http404
        
    def get(self, request, id):
        inscrito = self.get_object(id)
        serial = InscritosSerializer(inscrito)
        return Response(serial.data)
    
    def put (self, request, id):
        inscrito = self.get_object(id)
        serial = InscritosSerializer(inscrito, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.erros, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        inscrito = self.get_object(id)
        inscrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)