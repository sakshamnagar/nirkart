# Generated by Django 4.2.5 on 2023-12-27 13:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_alter_reviews_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
