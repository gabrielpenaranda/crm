# Generated by Django 4.2.2 on 2023-06-20 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Segmento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segmento', models.CharField(max_length=50, verbose_name='Segmento')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Segmento',
                'verbose_name_plural': 'Segmentos',
                'db_table': 'segmentos',
                'ordering': ['segmento'],
            },
        ),
        migrations.AlterModelOptions(
            name='actividad',
            options={'ordering': ['actividad'], 'verbose_name': 'Actividad', 'verbose_name_plural': 'Actividades'},
        ),
        migrations.AlterModelOptions(
            name='ciudad',
            options={'ordering': ['ciudad', 'estado'], 'verbose_name': 'Ciudad', 'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='estado',
            options={'ordering': ['estado', 'pais'], 'verbose_name': 'Estado', 'verbose_name_plural': 'Estados'},
        ),
        migrations.AlterModelOptions(
            name='pais',
            options={'ordering': ['pais'], 'verbose_name': 'Pais', 'verbose_name_plural': 'Paises'},
        ),
        migrations.AlterModelOptions(
            name='ramo',
            options={'ordering': ['ramo'], 'verbose_name': 'Ramo', 'verbose_name_plural': 'Ramos'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ['region'], 'verbose_name': 'Región', 'verbose_name_plural': 'Regiones'},
        ),
        migrations.AlterModelOptions(
            name='sector',
            options={'ordering': ['sector'], 'verbose_name': 'Sector', 'verbose_name_plural': 'Sectores'},
        ),
        migrations.AlterModelOptions(
            name='tamanoempresa',
            options={'ordering': ['tamano_empresa'], 'verbose_name': 'Tamaño de empresa', 'verbose_name_plural': 'Tamaños de empresa'},
        ),
        migrations.AlterModelOptions(
            name='tipocapital',
            options={'ordering': ['tipo_capital'], 'verbose_name': 'Tipo de capital', 'verbose_name_plural': 'Tiptipo_capitalos de capital'},
        ),
        migrations.AlterModelOptions(
            name='tipoempresa',
            options={'ordering': ['tipo_empresa'], 'verbose_name': 'Tipo de empresa', 'verbose_name_plural': 'Tipos de empresa'},
        ),
        migrations.AlterModelOptions(
            name='zona',
            options={'ordering': ['region', 'zona'], 'verbose_name': 'Zona', 'verbose_name_plural': 'Zonas'},
        ),
        migrations.RenameField(
            model_name='actividad',
            old_name='nombre',
            new_name='actividad',
        ),
        migrations.RenameField(
            model_name='ciudad',
            old_name='nombre',
            new_name='ciudad',
        ),
        migrations.RenameField(
            model_name='estado',
            old_name='nombre',
            new_name='estado',
        ),
        migrations.RenameField(
            model_name='pais',
            old_name='nombre',
            new_name='pais',
        ),
        migrations.RenameField(
            model_name='ramo',
            old_name='nombre',
            new_name='ramo',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='nombre',
            new_name='region',
        ),
        migrations.RenameField(
            model_name='sector',
            old_name='nombre',
            new_name='sector',
        ),
        migrations.RenameField(
            model_name='tamanoempresa',
            old_name='nombre',
            new_name='tamano_empresa',
        ),
        migrations.RenameField(
            model_name='tipocapital',
            old_name='nombre',
            new_name='tipo_capital',
        ),
        migrations.RenameField(
            model_name='tipoempresa',
            old_name='nombre',
            new_name='tipo_empresa',
        ),
        migrations.RenameField(
            model_name='vendedor',
            old_name='rif',
            new_name='numero_fiscal',
        ),
        migrations.RenameField(
            model_name='zona',
            old_name='nombre',
            new_name='zona',
        ),
    ]