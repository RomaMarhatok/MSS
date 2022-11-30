# Generated by Django 4.1.3 on 2022-11-28 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("userApp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="doctor",
            name="doctor_type",
        ),
        migrations.AddField(
            model_name="doctor",
            name="doctor_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="userApp.doctortype",
            ),
        ),
    ]