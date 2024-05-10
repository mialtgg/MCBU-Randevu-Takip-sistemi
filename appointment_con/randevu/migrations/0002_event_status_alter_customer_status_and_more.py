# Generated by Django 4.2.6 on 2024-04-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("randevu", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="status",
            field=models.CharField(
                choices=[
                    ("Active", "Aktif"),
                    ("Block", "İptal Edildi"),
                    ("Pasive", "Pasife Çekildi"),
                ],
                default=1,
                max_length=20,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="customer",
            name="status",
            field=models.CharField(
                choices=[
                    ("Active", "Aktif"),
                    ("Block", "İptal Edildi"),
                    ("Pasive", "Pasife Çekildi"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="status_description",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="meet",
            name="status",
            field=models.CharField(
                choices=[
                    ("Active", "Aktif"),
                    ("Block", "İptal Edildi"),
                    ("Block", "İptal Edildi"),
                ],
                max_length=20,
            ),
        ),
    ]