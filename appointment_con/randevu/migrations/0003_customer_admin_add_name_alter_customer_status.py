# Generated by Django 4.2.6 on 2023-12-23 06:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("randevu", "0002_customer_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="admin_add_name",
            field=models.CharField(
                choices=[
                    ("user1", "M.Müştak İLBAN"),
                    ("user2", "Nurdagül ERTÜRK"),
                    ("user3", "Pelin KOŞAN"),
                ],
                default=1,
                max_length=200,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="customer",
            name="status",
            field=models.CharField(
                choices=[("Active", "Aktif"), ("Block", "İptal Edildi")], max_length=20
            ),
        ),
    ]
