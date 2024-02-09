# Generated by Django 4.2.6 on 2024-02-01 22:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("randevu", "0011_rename_delated_appointment_customer_deleted"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customer",
            name="created_time",
            field=models.TimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]