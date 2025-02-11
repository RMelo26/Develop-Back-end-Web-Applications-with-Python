from django.db import models
from django.urls import reverse
from titulos.models import Titulos


# Modelo representando um Tipo de Atividade
class Instrutor(models.Model):
    """Modelo representando Instrutores"""
    id = models.AutoField(primary_key=True)
    rg = models.CharField(max_length=15, help_text="Informe o RG do Instrutor")
    nome = models.CharField(max_length=70, help_text="Informe o nome do Instrutor")
    dataNascimento = models.DateField(null=True, blank=True, help_text="Informe a data de nascimento do Instrutor")
    telefone = models.CharField(max_length=9, help_text="Informe o telefone do Instrutor")
    ddd = models.CharField(max_length=3, help_text="Informe o DDD do telefone do Instrutor")
    codigo_titulo = models.ForeignKey(Titulos, null=True, blank=True, on_delete=models.SET_NULL, db_column="titulo_codigo")
    
    def __str__(self):
        return f'{self.codigo} - {self.descricao}'