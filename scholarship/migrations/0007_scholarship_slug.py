# Generated by Django 5.1.4 on 2024-12-30 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0006_remove_scholarship_discipline'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
