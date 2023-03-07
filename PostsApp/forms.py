from django.forms import ModelForm
from django import forms
from .models import Post, Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['author']
        labels = {
            'post_img': 'Image front page'
        }

        widgets = {
            'title': forms.TextInput(attrs = {'class':'form-input', 'placeholder': 'This is the title '}),
            'subtitle': forms.TextInput(attrs = {'class':'form-input','placeholder': 'This is the subtitle'}),
             #quise cambiar estilos del boton de busqueda de archivos, pero no encontre   

        }      

 
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['post_id', 'username']
        widgets ={
            'comment': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Write your comment here... ', 'style':'width: 100%;height: 25%; margin-top: 0.5rem' }),
            
        }

 