# Generated by Django 5.0.6 on 2024-06-22 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_alter_etapa_options_alter_oportunidad_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oportunidad',
            name='descripcion',
        ),
    ]