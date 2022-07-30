from django.db import models

from .file_storage import ImageFileSystemStorage


class Shop(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)


class Img(models.Model):

    img = models.ImageField(upload_to="shop", storage=ImageFileSystemStorage())
    img_type = models.SmallIntegerField()
    name = models.ForeignKey("Shop", on_delete=models.CASCADE)
