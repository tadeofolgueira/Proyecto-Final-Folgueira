from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    apellido = forms.CharField(label='Apellido')
    mensaje = forms.CharField(widget=forms.Textarea, label='Mensaje')
    
class Registro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contrasenia",widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir contrasenia",widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {key: "" for key in fields}