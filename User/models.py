from django.db import models
from django.contrib.auth.models import User as UserAuth

class Avatar(models.Model):
    user = models.OneToOneField(UserAuth, on_delete= models.CASCADE)
    image = models.ImageField(upload_to='avatars', null=True, blank=True, default='blank.png')

    def __srt__(self):
        return self.user.username
