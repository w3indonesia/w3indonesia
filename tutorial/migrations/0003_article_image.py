# Generated by Django 5.1.4 on 2024-12-24 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0002_alter_article_options_alter_subcategory_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='articles/images/'),
        ),
    ]