# Generated by Django 4.1.5 on 2023-04-09 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_create_user_location_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserPersonalInfo",
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
                (
                    "first_name",
                    models.CharField(max_length=100, verbose_name="first name"),
                ),
                (
                    "second_name",
                    models.CharField(max_length=100, verbose_name="second name"),
                ),
                (
                    "patronymic",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="patronymic"
                    ),
                ),
                (
                    "email",
                    models.EmailField(blank=True, max_length=100, verbose_name="email"),
                ),
                (
                    "gender",
                    models.CharField(blank=True, default="Other", max_length=150),
                ),
                ("age", models.IntegerField(blank=True, default=-1)),
                ("health_status", models.TextField(blank=True, default="")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "user_personal_info",
            },
        ),
    ]
