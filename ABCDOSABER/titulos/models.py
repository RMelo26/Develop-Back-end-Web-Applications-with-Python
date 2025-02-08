from django.db import models
from django.urls import reverse

# Modelo representando um Tipo de Atividade
class Titulos(models.Model):
    """Modelo representando um Titulos"""
    codigo = models.AutoField(primary_key=True,
                                 help_text='Código do Titulos')
    descricao = models.CharField(max_length=70, null=False,
                                 help_text='Informe a descrição de Titulos')

    def __str__(self):
        return f'{self.codigo} - {self.descricao}'