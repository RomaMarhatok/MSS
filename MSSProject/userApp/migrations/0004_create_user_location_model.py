# Generated by Django 4.1.3 on 2022-12-23 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("userApp", "0003_create_user_personal_info_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserLocation",
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
                ("country", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "user_location",
            },
        ),
    ]
