from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import DatosUser

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
        
    #def clean_email(self):
        #email = self.cleaned_data.get("email")
        #return email
        
class EditarPerfil(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label = "Nombre")
    last_name = forms.CharField(label = "Apellido")
    avatar = forms.ImageField(required=False)
    sexo = forms.ChoiceField(choices=DatosUser.sexo_opciones,required=False)
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "avatar","sexo"]
        

class CambiarContrasenia(PasswordChangeForm):
    old_password = forms.CharField(label = "Contraseña actual",widget=forms.PasswordInput)
    new_password1 = forms.CharField(label = "Nueva contraseña",widget=forms.PasswordInput)
    new_password2 = forms.CharField(label = "Confirme nueva contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["old_password", "new_password1", "new_password2"]