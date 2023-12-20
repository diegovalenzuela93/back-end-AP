from rest_framework import serializers
from .models import instituciones, inscritos

class InstitucionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = instituciones
        fields = '__all__'
        
class InscritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = inscritos
        fields = '__all__'