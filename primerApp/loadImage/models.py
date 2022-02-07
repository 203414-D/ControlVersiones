

from django.db import models
from django.utils import timezone

class ImagenModelo(models.Model):
    name_img = models.CharField(max_length=255, null=False)
    url_img = models.CharField(max_length=255, null=False)
    format_img = models.CharField(max_length=255, null=False)
    created = models.DateTimeField(default=timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

class Meta:
    db_table ='imagen modelo'

class ImagenSave(models.Model):
    title = models.CharField(max_length=255, null=False)
    format =models.CharField(max_length=255, null=False)
    image = models.ImageField(null=True, blank=True, upload_to="assets/img/")

class meta:
    db_table ='imagenSave'