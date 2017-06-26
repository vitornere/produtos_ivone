from django.db import models


class Revista(models.Model):
    nome = models.CharField(max_length=30)
    validade = models.DateTimeField(blank=False)
    arquivo = models.FileField(blank=False, upload_to='revistas/')

    @staticmethod
    def __str__():
        return nome
