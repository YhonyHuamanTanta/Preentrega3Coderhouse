# Generated by Django 5.0.6 on 2024-07-26 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0014_atenderclinetes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atenderclinetes',
            old_name='lugar',
            new_name='llegada',
        ),
    ]
