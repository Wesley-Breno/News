from django.db import models
from django.utils import timezone


class Fonte(models.Model):
    nome = models.CharField(max_length=12)

    def __str__(self):
        return self.nome


class Post(models.Model):
    titulo = models.CharField(max_length=120)
    descricao = models.CharField(max_length=1000)
    fonte = models.ForeignKey(Fonte, on_delete=models.CASCADE)
    criacao = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.titulo
