# Generated by Django 4.2.6 on 2023-12-17 15:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("randevu", "0003_customer_delete_event"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="email",
        ),
        migrations.AddField(
            model_name="customer",
            name="konu",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]