# Generated by Django 4.2.5 on 2023-12-27 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_order_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
