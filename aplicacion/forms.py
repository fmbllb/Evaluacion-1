from django import forms
from aplicacion.models import Producto
# from .models import Usuario, Perfil
from .enumeraciones import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout , Submit , Div ,Field ,HTML



class UsuarioForm(UserCreationForm):
    email = forms.EmailField(label="Correo electrónico", widget=forms.EmailInput(attrs={"id": 'email'}))
    first_name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={"id": 'first_name'}))
    last_name = forms.CharField(label="Apellido", widget=forms.TextInput(attrs={"id": 'last_name'}))
    username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={"id": 'username'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={"id": 'password1'}))
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(attrs={"id": 'password2'}))
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

class FiltroCategoriaForm(forms.Form):
    categoria = forms.ChoiceField(choices=TIPO_PRODUCTO, required=False, label='Categoría')
    
    def __init__(self, *args, **kwargs):
        super(FiltroCategoriaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.add_input(Submit('submit', 'Filtrar'))


class DescripcionForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 10, 'cols': 80}),
        }


class StuffForm(UserCreationForm):
    username=forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={"id": 'username'}))
    is_staff=forms.BooleanField(label="Es administrador", widget=forms.CheckboxInput(attrs={"id": 'is_staff'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={"id": 'password1'}))
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(attrs={"id": 'password2'}))

class EmailUpdateForm(forms.ModelForm):
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={"id": 'password'}))

    class Meta:
        model = User
        fields = ['email']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(EmailUpdateForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not self.user.check_password(password):
            raise forms.ValidationError('La contraseña no es correcta')
        return password

#clase para actualizar el nombre de usuario
class UserUpdateForm(forms.ModelForm):
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={"id": 'password'}))

    class Meta:
        model = User
        fields = ['username']  # Cambiado a 'username' para actualizar el nombre de usuario

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(UserUpdateForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('Debe ingresar la contraseña')
        if not self.user.check_password(password):
            raise forms.ValidationError('La contraseña no es correcta')
        return password

    def save(self, commit=True):
        user = super(UserUpdateForm, self).save(commit=False)
        if commit:
            user.save()
        return user
""" 
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['telefono', 'direccion'] """
""" class UpdatePersonaForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut', 'numero_casa_departamento', 'direccion']

class LoginForm(forms.ModelForm):
    correo = forms.EmailField(label="Correo")
    contrasena = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['correo', 'contrasena'] """