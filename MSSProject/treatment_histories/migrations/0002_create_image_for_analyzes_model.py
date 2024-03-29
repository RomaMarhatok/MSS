# Generated by Django 4.1.5 on 2023-03-24 13:08

from django.db import migrations, models
import treatment_histories.models.image_for_analyzes


class Migration(migrations.Migration):

    dependencies = [
        ("treatment_histories", "0001_create_treatment_history_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImageForAnalyzes",
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
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=treatment_histories.models.image_for_analyzes.media_path_builder_for_analyzes_images,
                        verbose_name="image for analyzes",
                    ),
                ),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "image_for_analyzes",
            },
        ),
    ]
