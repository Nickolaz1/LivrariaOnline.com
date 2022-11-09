from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=30)
    valor = models.DecimalField(decimal_places=2, max_digits=6)
    descricao = models.TextField()
    capa = models.CharField(max_length=200)
    insert = models.DateTimeField()
    update = models.DateTimeField()
    