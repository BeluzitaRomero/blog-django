from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Avatar

class UserCreationForm(UserCreationForm):
    username = forms.CharField(label = 'Username', widget= forms.TextInput(attrs = {'class':'form-input'}))
    email = forms.EmailField(widget= forms.TextInput(attrs = {'class':'form-input'}))
    password1 = forms.CharField(label = 'Password', widget= forms.PasswordInput(attrs = {'class':'form-input'}))
    password2 = forms.CharField(label = 'Repeat password', widget = forms.PasswordInput(attrs = {'class':'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}


class UserEditForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput(attrs = {'class':'form-input'}))
    email = forms.EmailField(widget= forms.TextInput(attrs = {'class':'form-input'}))
    first_name = forms.CharField(widget= forms.TextInput(attrs = {'class':'form-input'}))
    last_name= forms.CharField(widget= forms.TextInput(attrs = {'class':'form-input'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        help_texts = {k:'' for k in fields}
       


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = '__all__'
        exclude = ['user']



# Hago este custom para poder dar estilos al formulario que me 
# crea automaticamente el AutehticationForm
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-input'
        self.fields['password'].widget.attrs['class'] = 'form-input'