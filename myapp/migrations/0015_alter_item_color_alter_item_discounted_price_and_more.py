# Generated by Django 4.2.5 on 2023-12-11 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_delete_deliverycharges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='color',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='item',
            name='discounted_price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='item',
            name='manufacturing_brand',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='item',
            name='model_name',
            field=models.CharField(max_length=100),
        ),
    ]
