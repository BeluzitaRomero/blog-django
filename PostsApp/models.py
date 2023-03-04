from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250, null=True, blank=True, default='')
    post_description = RichTextUploadingField(null=True, blank=True)
    post_img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title