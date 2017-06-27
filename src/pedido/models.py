from django.db import models
from django.contrib.auth.models import User


class Pedido(models.Model):
    cliente = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    lista = models.TextField(
        null=True
    )

    def criar_pedido(self, cliente, lista):
        lista_serializada = lista
        return self.objects.create(cliente=cliente, lista=lista_serializada)

    def salvar_pedido(self, cliente, lista):
        lista_serializada = lista
        self.save(cliente, lista)

    def get_lista(self):
        lista_serializada = self.lista
        return lista_serializada

    @staticmethod
    def __str__():
        return get_lista()
