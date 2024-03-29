# Generated by Django 4.1.5 on 2023-05-01 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("treatment_histories", "0008_add_related_names"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="imageforanalyzes",
            options={
                "verbose_name": "Изображение для анализа",
                "verbose_name_plural": "Изображения для анализа",
            },
        ),
        migrations.AlterModelOptions(
            name="treatmenthistory",
            options={
                "verbose_name": "История лечения",
                "verbose_name_plural": "Истории лечения",
            },
        ),
        migrations.AlterModelOptions(
            name="treatmenthistorydocument",
            options={
                "verbose_name": "Прилогающийся документ",
                "verbose_name_plural": "Прилогающиеся документы",
            },
        ),
        migrations.AlterModelOptions(
            name="treatmenthistoryimageforanalyzes",
            options={
                "verbose_name": "Прилогающиеся изображение",
                "verbose_name_plural": "Прилогающиеся изображения",
            },
        ),
    ]
