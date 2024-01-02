# Generated by Django 4.2.5 on 2023-12-15 16:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_address_address_unique_primary_per_customer'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('status', models.CharField(choices=[('orderplaced', 'orderplaced'), ('orderconfirmed', 'orderconfirmed'), ('ordershipped', 'ordershipped'), ('ordercancelled', 'ordercancelled')], default='orderplaced', max_length=50)),
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_id', models.CharField(max_length=15)),
                ('item_name', models.CharField(max_length=15)),
                ('item_price', models.IntegerField()),
                ('item_discounted_price', models.IntegerField()),
                ('item_discount', models.IntegerField()),
                ('item_vendor', models.CharField(max_length=50)),
                ('address1', models.CharField(max_length=50)),
                ('address2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=6, validators=[django.core.validators.MinLengthValidator(6)])),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='account.userprofile')),
            ],
        ),
    ]