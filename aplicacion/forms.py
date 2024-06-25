from django import forms
from .models import Usuario, Perfil
from .enumeraciones import *
from django.contrib.auth.forms import UserCreationForm


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['telefono', 'direccion']

class UsuarioForm(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={"id": 'username'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={"id": 'password1'}))
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(attrs={"id": 'password2'}))

class UpdatePersonaForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut', 'numero_casa_departamento', 'direccion']

class LoginForm(forms.ModelForm):
    correo = forms.EmailField(label="Correo")
    contrasena = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['correo', 'contrasena']