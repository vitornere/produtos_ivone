from django.db import models
from django.utils import timezone


class Revista(models.Model):
    nome = models.CharField(max_length=99)
    validade = models.DateTimeField(blank=False)
    arquivo = models.FileField(blank=False, upload_to='revistas/')
