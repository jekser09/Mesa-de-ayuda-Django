# Generated by Django 4.2.1 on 2023-05-18 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SoporteTecnico', '0005_solicitud'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='observacion',
            field=models.TextField(blank=True, default=''),
        ),
    ]
