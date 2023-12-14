# forms.py
from django import forms
from .models import Cita  

class CitaForm(forms.ModelForm):
    servicio = forms.ChoiceField(choices=Cita.opciones_consultas, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Cita
        fields = ['servicio', 'nombre_del_cliente', 'direccion', 'fecha', 'hora_inicio', 'descripcion', 'celular']

        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'celular': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'nombre_del_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }
