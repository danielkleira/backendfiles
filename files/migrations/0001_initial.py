# Generated by Django 4.1.2 on 2022-10-05 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Files",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tipo", models.CharField(max_length=255)),
                ("data", models.CharField(max_length=255)),
                ("valor", models.CharField(max_length=255)),
                ("cpf", models.CharField(max_length=255)),
                ("cartao", models.CharField(max_length=255)),
                ("hora", models.CharField(max_length=255)),
                ("dono_da_loja", models.CharField(max_length=255)),
                ("nome_loja", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="UpFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("upFile", models.FileField(upload_to="files/upFiles/")),
            ],
        ),
    ]
