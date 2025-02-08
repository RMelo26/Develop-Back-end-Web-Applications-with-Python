from django.db import models
from django.urls import reverse

# Modelo representando um Tipo de Atividade
class alunos(models.Model):
    """Modelo representando um Tipo de Atividade"""
    codigo = models.AutoField(primary_key=True,
                                 help_text='Código do Tipo de Atividade')
    descricao = models.CharField(max_length=100, null=False,
                                 help_text='Informe a descrição do Tipo de Atividade')

    def __str__(self):
        return f'{self.codigo} - {self.descricao}'