# Generated by Django 5.1.3 on 2024-12-10 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
