# Generated by Django 4.2.5 on 2023-09-08 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terceros', '0003_alter_tercero_tipo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipotercero',
            options={'ordering': ['descripcion'], 'verbose_name': 'Tipo de tercero', 'verbose_name_plural': 'Tipos de terceros'},
        ),
    ]
