# Generated by Django 4.2.5 on 2023-12-07 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_vendor_user'),
        ('myapp', '0009_remove_item_tag1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='vendor',
            field=models.ForeignKey(default='pk=1', on_delete=django.db.models.deletion.CASCADE, related_name='item', to='account.vendor'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='myapp.category'),
        ),
    ]
