# Generated by Django 5.1.2 on 2024-11-26 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_category_tag_alter_news_options_news_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='author',
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='news_items', to='news.tag'),
        ),
    ]
