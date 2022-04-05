from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class ProfileTabla(models.Model):
    user_id = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    url_img = models.ImageField(null=True,blank=True, default='', upload_to="assets/img_profile")
