# Generated by Django 4.2.7 on 2024-01-11 09:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resume", "0008_resume_experience"),
    ]

    operations = [
        migrations.AddField(
            model_name="resume",
            name="current_position",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="resume",
            name="phone_no",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]