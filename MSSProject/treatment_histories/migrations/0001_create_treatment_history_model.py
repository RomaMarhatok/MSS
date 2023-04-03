# Generated by Django 4.1.5 on 2023-03-24 13:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("doctor", "0004_create_doctor_doctor_specialization_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="TreatmentHistory",
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
                ("title", models.TextField(blank=True)),
                ("short_description", models.TextField(blank=True)),
                ("description", models.TextField()),
                ("conclusion", models.TextField(blank=True)),
                ("date", models.DateTimeField(default=datetime.datetime.now)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "doctor",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="doctor.doctor",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "treatment_history",
            },
        ),
    ]