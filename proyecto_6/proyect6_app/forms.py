from django import forms
from . import models

class registroProyecto(forms.ModelForm):
    class Meta:
        model = models.Proyecto
        fields = '__all__'