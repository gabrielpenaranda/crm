# Generated by Django 4.2.2 on 2023-08-26 16:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("terceros", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tercero",
            name="tipo",
            field=models.CharField(
                choices=[
                    ("CT", "Contacto"),
                    ("SP", "Suspecto"),
                    ("LD", "Lead"),
                    ("OP", "Oportunidad"),
                    ("PR", "Prospecto"),
                    ("CL", "CLiente"),
                ],
                default="CT",
                max_length=2,
            ),
        ),
        migrations.AddIndex(
            model_name="tercero",
            index=models.Index(fields=["nombre"], name="terceros_nombre_d2429c_idx"),
        ),
    ]
