# Generated by Django 2.2.10 on 2020-05-19 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feriado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feriadomodel',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, verbose_name='modificado em'),
        ),
    ]
