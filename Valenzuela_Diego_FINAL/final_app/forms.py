from django import forms
from final_app import models

estados = [('reservado','Reservado'),('completada','Completada'),('anulada','Anulada'),('no asisten','No Asisten')]

class formInscripciones(forms.ModelForm):
    class Meta:
        model = models.inscritos
        fields = ['nombre','telefono','fecha','institucion','hora','observacion','estado']
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.NumberInput(attrs={'class':'form-control'}),
            'fecha':forms.DateInput(attrs={'class':'form-control', 'type':'Date'}),
            'institucion':forms.Select(attrs={'class':'form-select'}),
            'hora':forms.TimeInput(attrs={'class':'form-control', 'type':'Time'}),
            'observacion':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.Select(attrs={'class':'form-select'},choices=estados)
        }
        
        
class formInstituciones(forms.ModelForm):
    class Meta:
        model = models.instituciones
        fields = ['nombre',]
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'})
        }