# Generated by Django 4.2.18 on 2025-02-05 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipodeatividade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipodeatividade',
            name='descricao',
            field=models.CharField(help_text='Informe a descrição do Tipo de Atividade', max_length=100),
        ),
    ]
