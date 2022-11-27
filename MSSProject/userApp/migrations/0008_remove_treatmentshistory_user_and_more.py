# Generated by Django 4.1.3 on 2022-11-27 10:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userApp", "0007_rename_doctors_doctor_rename_patients_patient"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="treatmentshistory",
            name="user",
        ),
        migrations.AddField(
            model_name="treatmentshistory",
            name="patient",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="userApp.patient",
            ),
        ),
    ]
