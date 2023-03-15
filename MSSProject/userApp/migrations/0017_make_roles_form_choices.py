# Generated by Django 4.1.5 on 2023-03-11 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userApp", "0016_change_treatment_history_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="role",
            name="name",
            field=models.CharField(
                choices=[("DOCTOR", "Doctor"), ("PATIENT", "Patient")],
                max_length=100,
                unique=True,
                verbose_name="role name",
            ),
        ),
    ]