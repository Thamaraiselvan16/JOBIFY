# Generated by Django 4.2.7 on 2024-01-10 04:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("job", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="salary",
            field=models.PositiveIntegerField(default=3),
        ),
    ]