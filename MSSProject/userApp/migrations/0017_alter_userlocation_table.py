# Generated by Django 4.1.3 on 2022-12-20 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("userApp", "0016_userpersonalinfo_age_userpersonalinfo_gender_and_more"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="userlocation",
            table="user_location",
        ),
    ]
