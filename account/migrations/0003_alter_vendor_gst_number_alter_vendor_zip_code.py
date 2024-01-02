# Generated by Django 4.2.5 on 2023-12-02 08:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_vendor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='gst_number',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(15)]),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='zip_code',
            field=models.CharField(max_length=6, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
    ]