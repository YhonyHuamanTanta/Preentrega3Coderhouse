# Generated by Django 5.0.6 on 2024-07-01 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0005_entregables_dni'),
    ]

    operations = [
        migrations.AddField(
            model_name='entregables',
            name='apellido',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
