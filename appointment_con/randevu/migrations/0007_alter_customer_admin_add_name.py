# Generated by Django 4.2.6 on 2023-12-24 16:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("randevu", "0006_alter_customer_admin_add_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="admin_add_name",
            field=models.CharField(
                choices=[
                    ("user1", "M.Müştak İLBAN"),
                    ("user2", "Nurdagül ERTÜRK"),
                    ("user3", "Pelin KOŞAN"),
                    ("user4", "Aysun KOŞAN"),
                ],
                max_length=200,
            ),
        ),
    ]
