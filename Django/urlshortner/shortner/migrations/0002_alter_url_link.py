# Generated by Django 5.0.6 on 2024-07-15 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shortner", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="url",
            name="link",
            field=models.CharField(max_length=100000),
        ),
    ]
