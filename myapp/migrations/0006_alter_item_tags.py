# Generated by Django 4.2.5 on 2023-12-05 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_item_tag_item_tags_alter_item_tag1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='tags',
            field=models.CharField(max_length=100),
        ),
    ]
