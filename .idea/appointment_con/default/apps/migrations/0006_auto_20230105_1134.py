# Generated by Django 3.2 on 2023-01-05 06:04

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_auto_20230105_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crmcontact',
            name='tags',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Exiting'), (2, 'Lead'), (3, 'Long-term'), (4, 'Partner')], max_length=50),
        ),
        migrations.AlterField(
            model_name='crmlead',
            name='tags',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Exiting'), (2, 'Lead'), (3, 'Long-term'), (4, 'Partner')], max_length=50),
        ),
    ]
