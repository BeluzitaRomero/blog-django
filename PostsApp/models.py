from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from datetime import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250, null=True, blank=True, default='')
    post_description = RichTextUploadingField(null=True, blank=True)
    post_img = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=140)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)