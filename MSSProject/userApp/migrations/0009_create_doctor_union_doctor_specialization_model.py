# Generated by Django 4.1.3 on 2022-12-23 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("userApp", "0008_create_doctor_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="DoctorDoctorSpecialization",
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
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="doctor_doctor_specialization",
                        to="userApp.doctor",
                    ),
                ),
                (
                    "doctor_specialization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="doctor_doctor_specialization",
                        to="userApp.doctorspecialization",
                    ),
                ),
            ],
            options={
                "db_table": "doctor_doctor_specialization",
            },
        ),
    ]
