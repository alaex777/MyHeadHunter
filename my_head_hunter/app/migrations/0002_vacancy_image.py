# Generated by Django 4.1.7 on 2023-02-23 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="vacancy",
            name="image",
            field=models.ImageField(blank=True, upload_to=""),
        ),
    ]
