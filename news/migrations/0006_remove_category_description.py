# Generated by Django 5.1.3 on 2024-12-08 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
    ]
