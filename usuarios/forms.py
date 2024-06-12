from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    apellido = forms.CharField(label='Apellido')
    mensaje = forms.CharField(widget=forms.Textarea, label='Mensaje')