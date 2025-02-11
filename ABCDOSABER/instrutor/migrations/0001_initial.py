# Generated by Django 4.2.18 on 2025-02-11 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('titulos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrutor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rg', models.CharField(help_text='Informe o RG do Instrutor', max_length=15)),
                ('nome', models.CharField(help_text='Informe o nome do Instrutor', max_length=70)),
                ('dataNascimento', models.DateField(blank=True, help_text='Informe a data de nascimento do Instrutor', null=True)),
                ('telefone', models.CharField(help_text='Informe o telefone do Instrutor', max_length=9)),
                ('ddd', models.CharField(help_text='Informe o DDD do telefone do Instrutor', max_length=3)),
                ('codigo_titulo', models.ForeignKey(blank=True, db_column='titulo_codigo', null=True, on_delete=django.db.models.deletion.SET_NULL, to='titulos.titulos')),
            ],
        ),
    ]
