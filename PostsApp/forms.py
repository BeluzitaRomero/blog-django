from django.forms import ModelForm
from django import forms
from .models import Post, Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['author']

        widgets = {
            'title': forms.TextInput(attrs = {'class':'form-input', 'placeholder': 'This is the title of the post'}),
            'subtitle': forms.TextInput(attrs = {'class':'form-input'}),
            
            
        }

 
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['post_id', 'username']
        widgets ={
            'comment': forms.Textarea(attrs={'class': 'form-control', 'style':'width: 100%;height: 25%; margin-top: 0.5rem' }),
            
        }

        # widgets = {
        #     'title': forms.TextInput(attrs = {'class':'form-input', 'placeholder': 'This is the title of the post'}),
        #     'subtitle': forms.TextInput(attrs = {'class':'form-input'}),
            
            
        # }

 