from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar

class UserCreationForm(UserCreationForm):

    username = forms.CharField(label = 'Nombre de usuario', widget= forms.TextInput)
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label = 'Repetir contraseña', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}


class UserEditForm(forms.Form):
    username = forms.CharField(label = 'Nombre de usuario', widget= forms.TextInput)
    email = forms.EmailField(label='Modificar email')
    first_name = forms.CharField(label='Nombre')
    last_name= forms.CharField(label='Apellido')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        help_texts = {k:'' for k in fields}


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = '__all__'
        exclude = ['user']