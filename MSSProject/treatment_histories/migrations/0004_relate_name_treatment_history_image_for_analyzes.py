# Generated by Django 4.1.5 on 2023-04-07 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "treatment_histories",
            "0003_create_treatment_history_union_image_for_analyzes_model",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="treatmenthistoryimageforanalyzes",
            name="image_for_analyzes",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="treatment_history_image_for_analyzes",
                to="treatment_histories.imageforanalyzes",
            ),
        ),
        migrations.AlterField(
            model_name="treatmenthistoryimageforanalyzes",
            name="treatment_history",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="treatment_history_image_for_analyzes",
                to="treatment_histories.treatmenthistory",
            ),
        ),
    ]
