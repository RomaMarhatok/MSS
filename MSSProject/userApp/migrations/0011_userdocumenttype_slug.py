# Generated by Django 4.1.3 on 2022-12-14 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userApp", "0010_userdocumenttype_userdocument_document_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="userdocumenttype",
            name="slug",
            field=models.SlugField(default="default slug", max_length=100),
            preserve_default=False,
        ),
    ]