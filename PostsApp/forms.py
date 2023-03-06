from django.forms import ModelForm
from django import forms
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['author']

        widgets = {
            'title': forms.TextInput(attrs = {'class':'form-input', 'placeholder': 'This is the title of the post'}),
            'subtitle': forms.TextInput(attrs = {'class':'form-input'}),
            
            
        }

 