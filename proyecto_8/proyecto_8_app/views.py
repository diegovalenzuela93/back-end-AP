from django.shortcuts import render
from .models import Estudiantes
from .serializers import EstudiantesSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from django.http import Http404

# Create your views here.
@api_view(['GET', 'POST'])
def estudiantes_list(request):
    if request.method == 'GET':
        estudi = Estudiantes.objects.all()
        serial = EstudiantesSerializer(estudi, many=True)
        return Response(serial.data)
    
    if request.method == 'POST':
        serial = EstudiantesSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def estudiante_detalle(request, id):
    try:
        estudi = Estudiantes.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = EstudiantesSerializer(estudi)
        return Response(serial.data)
    
    if request.method == 'PUT':
        serial = EstudiantesSerializer(estudi, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        estudi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#CLASS BASE VIEWS

class EstudianteList_class(APIView):
    def get(self, request):
        estudi = Estudiantes.objects.all()
        serial = EstudiantesSerializer(estudi, many=True)
        return Response(serial.data)
    
    def post(self,request):
        serial = EstudiantesSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Estudiante_detalle_class(APIView):
    def get_object(self, id):
        try:
            return Estudiantes.objects.get(pk=id)
        except Estudiantes.DoesNotExist:
            return Http404
        
    def get(self, request, id):
        estude = self.get_object(id)
        serial = EstudiantesSerializer(estude)
        return Response(serial.data)
    
    def put (self, request, id):
        estude = self.get_object(id)
        serial = EstudiantesSerializer(estude, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.erros, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        estude = self.get_object(id)
        estude.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)