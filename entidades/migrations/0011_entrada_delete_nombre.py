# Generated by Django 5.0.6 on 2024-07-17 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0010_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Nombre',
        ),
    ]
