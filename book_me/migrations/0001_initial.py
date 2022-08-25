# Generated by Django 4.1 on 2022-08-24 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Artista",
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
                ("nombre", models.CharField(max_length=255)),
                ("estilo", models.CharField(max_length=255)),
                ("precio_de_contratacion", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Lugar",
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
                ("nombre", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Evento",
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
                ("nombre", models.CharField(max_length=255)),
                ("fecha", models.DateField()),
                ("tiene_vip", models.BooleanField(default=False)),
                ("capacidad_general", models.IntegerField()),
                ("capacidad_sector_vip", models.IntegerField(default=0)),
                ("entradas_general_vendidas", models.IntegerField(default=0)),
                ("entradas_vip_vendidas", models.IntegerField(default=0)),
                ("precio_entrada_general", models.FloatField()),
                ("precio_entrada_vip", models.FloatField(default=0)),
                (
                    "artista",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="eventos",
                        to="book_me.artista",
                    ),
                ),
                (
                    "lugar",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="book_me.lugar",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Entrada",
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
                ("vip", models.BooleanField()),
                ("email_comprador", models.EmailField(max_length=254)),
                ("secure_token", models.CharField(max_length=80)),
                (
                    "evento",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="entradas_vendidas",
                        to="book_me.evento",
                    ),
                ),
            ],
        ),
    ]
