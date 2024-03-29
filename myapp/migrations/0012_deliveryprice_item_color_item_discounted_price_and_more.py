# Generated by Django 4.2.5 on 2023-12-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_item_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='color',
            field=models.CharField(default='red', max_length=15),
        ),
        migrations.AddField(
            model_name='item',
            name='discounted_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AddField(
            model_name='item',
            name='manufacturing_brand',
            field=models.CharField(default=1, max_length=50),
        ),
        migrations.AddField(
            model_name='item',
            name='model_name',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
