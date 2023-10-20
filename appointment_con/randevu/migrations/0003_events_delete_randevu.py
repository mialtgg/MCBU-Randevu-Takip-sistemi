# Generated by Django 4.2.6 on 2023-10-20 07:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("randevu", "0002_randevu_oncelik_randevu_saatf_randevu_saats"),
    ]

    operations = [
        migrations.CreateModel(
            name="Events",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("start", models.DateTimeField(blank=True, null=True)),
                ("end", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Randevu",
        ),
    ]
