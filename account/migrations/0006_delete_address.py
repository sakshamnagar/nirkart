# Generated by Django 4.2.5 on 2023-12-15 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_address_address_unique_primary_per_customer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
    ]
