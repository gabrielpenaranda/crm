# Generated by Django 5.0.6 on 2024-06-22 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_remove_oportunidad_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oportunidad',
            name='status',
        ),
    ]