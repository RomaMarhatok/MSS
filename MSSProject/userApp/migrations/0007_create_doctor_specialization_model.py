# Generated by Django 4.1.3 on 2022-12-23 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userApp", "0006_create_document_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="DoctorSpecialization",
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
                ("slug", models.SlugField(max_length=100, unique=True)),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        unique=True,
                        verbose_name="doctor profession name",
                    ),
                ),
            ],
            options={
                "db_table": "doctor_specialization",
            },
        ),
    ]
