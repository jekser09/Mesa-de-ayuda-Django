# Generated by Django 4.2.1 on 2023-05-18 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SoporteTecnico', '0002_sede_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
                ('observacion', models.TextField(blank=True, default='')),
                ('resuelto', models.BooleanField(default=False)),
                ('idarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SoporteTecnico.area')),
                ('idpersona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]