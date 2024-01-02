# Generated by Django 4.2.5 on 2023-12-05 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_category_slug_alter_item_tag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='slug'),
        ),
        migrations.AlterField(
            model_name='item',
            name='tag',
            field=models.TextField(default='tag', max_length=200),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(default='slug'),
        ),
    ]