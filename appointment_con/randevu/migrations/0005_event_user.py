# Generated by Django 4.2.6 on 2024-02-29 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("randevu", "0004_customer_appointment_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_id",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
