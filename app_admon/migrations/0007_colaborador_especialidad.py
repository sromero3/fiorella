# Generated by Django 5.0.6 on 2024-06-25 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_admon', '0006_especialidad_colaborador'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='especialidad',
            field=models.ManyToManyField(to='app_admon.especialidad'),
        ),
    ]
