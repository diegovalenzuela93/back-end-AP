from django import forms 
from django.core import validators

class registroEmpleados(forms.Form):
    ESTADOS = [('activo', 'ACTIVO'), ('inactivo', 'INACTIVO'), ('bloqueado', 'BLOQUEADO')]
    
    nombre = forms.CharField(validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(20)])
    email = forms.CharField(widget=forms.EmailInput)
    fono = forms.IntegerField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))
    
    nombre.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    fono.widget.attrs['class'] = 'form-control'
    password.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-select'