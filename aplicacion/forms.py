from django import forms
from .models import *
from django.core.exceptions import ValidationError
# from .models import Usuario, Perfil
from .enumeraciones import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout , Submit , Div ,Field ,HTML
from aplicacion import static



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

#Clase para actualizar el correo electrónico
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

#Clase para actualizar el teléfono
class PhoneUpdateForm(forms.ModelForm):
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = Perfil  # Asegúrate de que el modelo sea tu modelo de Perfil
        fields = ['telefono']  # Campos que quieres actualizar en el perfil

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not self.user.check_password(password):
            raise forms.ValidationError('La contraseña no es válida.')
        return password

    def save(self, commit=True):
        perfil = super().save(commit=False)
        perfil.usuario = self.user  # Asignar el usuario al perfil
        if commit:
            perfil.save()
        return perfil
    
#Clase para actualizar la direccion
class DirectionUpdateForm(forms.ModelForm):
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = Perfil  # Asegúrate de que el modelo sea tu modelo de Perfil
        fields = ['direccion']  # Campos que quieres actualizar en el perfil

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not self.user.check_password(password):
            raise forms.ValidationError('La contraseña no es válida.')
        return password

    def save(self, commit=True):
        perfil = super().save(commit=False)
        perfil.usuario = self.user  # Asignar el usuario al perfil
        if commit:
            perfil.save()
        return perfil
    
class EditarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'categoria_producto', 'foto']
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio',
            'descripcion': 'Descripción',
            'categoria_producto': 'Categoría',
            'foto': 'Foto del producto'
        }
        widgets = {
            'nombre': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            'descripcion': forms.Textarea(attrs={'rows': 10, 'cols': 110}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EditarProductoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('nombre', css_class='form-control mb-3'),
            Field('precio', css_class='form-control mb-3'),
            Div(
                'descripcion',
                css_class='mb-3'
            ),
            Field('categoria_producto', css_class='form-control mb-3'),
            Field('foto', css_class='form-control mb-3'),
            Div(
                Submit('submit', 'Guardar Cambios', css_class='btn btn-primary mr-2'),
                HTML('<a href="{% url \'productosadmin\' %}" class="btn btn-secondary mr-2">Cancelar</a>'),
                css_class='d-flex justify-content-between mt-3'
            ),
        )

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is None:
            raise ValidationError('Este campo es obligatorio.')
        if precio < 0:
            raise ValidationError('El precio no puede ser negativo.')
        return precio

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        descripcion = cleaned_data.get("descripcion")
        categoria_producto = cleaned_data.get("categoria_producto")

        if not nombre:
            self.add_error('nombre', 'Este campo es obligatorio.')
        if not descripcion:
            self.add_error('descripcion', 'Este campo es obligatorio.')
        if not categoria_producto:
            self.add_error('categoria_producto', 'Este campo es obligatorio.')

        return cleaned_data
    

class AgregarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'categoria_producto', 'foto']