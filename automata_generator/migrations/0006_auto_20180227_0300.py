# Generated by Django 2.0.2 on 2018-02-27 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automata_generator', '0005_auto_20180227_0300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='automatatransition',
            old_name='transition_to',
            new_name='transitionto',
        ),
    ]
