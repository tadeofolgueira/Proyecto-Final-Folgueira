from django import forms
from .models import Casa


class BusquedaCasas(forms.Form):
    tipo = forms.CharField(max_length= 20)
