from django import forms
from .models import Reservas
from django.core import validators

class FormularioReserva(forms.ModelForm):
    estados = [('Reservado', 'RESERVADO'), ('Completada', 'COMPLETADA'), ('Anulada', 'ANULADA'), ('No Asisten', 'NO ASISTEN')]
    
    nombre = forms.CharField(validators=[validators.MaxLengthValidator(80, message='El nombre no puede exceder los 80 caracteres')])
    telefono = forms.IntegerField()
    email = forms.EmailField(validators=[validators.EmailValidator(message='Debe ingresar un email valido')])
    fechaReserva = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}), label='Fecha de Reserva')
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'type':'time'}))
    NumPersonas = forms.IntegerField(validators=[validators.MinValueValidator(1, message='El numero de personas debe ser mayor a 0'), validators.MaxValueValidator(15, message='El numero de personas no debe ser mayor a 15')], label='Numero de Personas')
    estado = forms.CharField(widget=forms.Select(choices=estados))
    observacion = forms.CharField(required=False)
    
    nombre.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    fechaReserva.widget.attrs['class'] = 'form-control'
    hora.widget.attrs['class'] = 'form-control'
    NumPersonas.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-select'
    observacion.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Reservas
        fields = '__all__'
    
