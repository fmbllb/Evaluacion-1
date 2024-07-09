from django import forms
from .models import *
from django.core.exceptions import ValidationError
# from .models import Usuario, Perfil
from .enumeraciones import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout , Submit , Div ,Field ,HTML, ButtonHolder
from aplicacion import static



#CRUD PEDIDOS
#Formulario para la compra del pedido
class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['usuario', 'productos', 'fecha_compra', 'boleta', 'total', 'estado_entrega']

#Formulario para el detalle de la compra
class DetalleCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleCompra
        fields = ['cantidad']

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
    
#Editar usuario
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff']

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
    
class DirectionUpdateForm(forms.ModelForm):
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = Perfil
        fields = ['direccion']

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
    eliminar = forms.BooleanField(required=False, widget=forms.HiddenInput(), initial=False)

    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'categoria_producto', 'foto', 'stock']


        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Producto'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descripción'}),
            'categoria_producto': forms.Select(attrs={'class': 'form-control'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'nombre',
            'precio',
            'descripcion',
            'categoria_producto',
            'foto',
            'stock',  # Agregar el campo stock al formulario
            ButtonHolder(
                Submit('submit', 'Guardar cambios', css_class='btn btn-primary mr-2'),
                HTML('<button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#confirmDeleteModal">Eliminar producto</button>'),
                css_class='mt-3'
            )
        )

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is None:
            raise forms.ValidationError("El precio del producto es obligatorio.")
        try:
            precio_int = int(precio)
            if precio_int <= 0:
                raise forms.ValidationError("El precio del producto debe ser mayor que cero.")
        except ValueError:
            raise forms.ValidationError("Por favor ingresa un número válido para el precio.")

        return precio

class AgregarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'categoria_producto', 'foto']
        labels = {
            'nombre': 'Nombre del Producto',
            'precio': 'Precio',
            'descripcion': 'Descripción',
            'categoria_producto': 'Categoría del Producto',
            'foto': 'Imagen del Producto',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Producto'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descripción'}),
            'categoria_producto': forms.Select(attrs={'class': 'form-control'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }
        error_messages = {
            'nombre': {
                'required': "Por favor ingrese el nombre del producto.",
            },
            'precio': {
                'required': "Por favor ingrese el precio del producto.",
                'min_value': "El precio no puede ser negativo.",
            },
            'descripcion': {
                'required': "Por favor ingrese la descripción del producto.",
            },
            'categoria_producto': {
                'required': "Por favor seleccione la categoría del producto.",
            },
            'foto': {
                'required': "Por favor seleccione una imagen para el producto.",
            },
        }
        
