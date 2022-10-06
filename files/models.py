from django.db import models
from distutils.command.upload import upload


class Files(models.Model):
    tipo = models.CharField(max_length=255)
    data = models.CharField(max_length=255)
    valor = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255)
    cartao = models.CharField(max_length=255)
    hora = models.CharField(max_length=255)
    dono_da_loja = models.CharField(max_length=255)
    nome_loja = models.CharField(max_length=255)


class UpFile(models.Model):
    upFile = models.FileField(upload_to="upFiles/")
