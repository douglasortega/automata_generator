# Generated by Django 2.0.2 on 2018-02-22 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automata_generator', '0003_remove_automatatest_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='automatatest',
            name='test',
            field=models.TextField(blank=True, help_text='Ingrese cadenas de prueba separadas por una "," ', verbose_name='Cadenas de Prueba'),
        ),
    ]