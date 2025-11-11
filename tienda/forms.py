from django import forms
from .models import Camiseta, Equipo, Cliente

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'pais', 'escudo']

class CamisetaForm(forms.ModelForm):
    class Meta:
        model = Camiseta
        fields = ['equipo', 'jugador', 'numero', 'precio', 'foto_frente', 'foto_espalda']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email']

class BusquedaCamisetaForm(forms.Form):
    consulta = forms.CharField(
        label="Buscar camiseta (jugador / equipo / número)",
        max_length=100,
        required=False,
    )

