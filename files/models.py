from django.db import models
from distutils.command.upload import upload


class Files(models.Model):
    typeOf = models.CharField(max_length=255)
    data = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255)
    card = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    store = models.CharField(max_length=255)


class UpFile(models.Model):
    upFile = models.FileField(upload_to="upFiles/")
