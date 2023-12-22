# Generated by Django 4.2.6 on 2023-10-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("last_name", models.CharField(max_length=100)),
                ("first_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
            ],
        ),
    ]
