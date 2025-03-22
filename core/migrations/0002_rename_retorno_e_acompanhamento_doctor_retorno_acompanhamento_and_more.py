# Generated by Django 5.1.7 on 2025-03-22 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='retorno_e_acompanhamento',
            new_name='retorno_acompanhamento',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='descricao',
            field=models.TextField(help_text='Descreva o médico como pessoa.'),
        ),
    ]
