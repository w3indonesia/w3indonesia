# Generated by Django 5.1.4 on 2025-01-03 15:04

import ckeditor.fields
import django.db.models.deletion
import focuus.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, validators=[focuus.models.validate_unicode])),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField(max_length=100, unique=True, validators=[focuus.models.validate_unicode])),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, validators=[focuus.models.validate_unicode])),
                ('description', models.TextField(blank=True)),
                ('requirements', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('final_product_description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=100, unique=True, validators=[focuus.models.validate_unicode])),
                ('order', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='focuus.category')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stages', to='focuus.project')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, validators=[focuus.models.validate_unicode])),
                ('slug', models.SlugField(max_length=100, validators=[focuus.models.validate_unicode])),
                ('content', ckeditor.fields.RichTextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish')], default='draft', max_length=10)),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='focuus.stage')),
            ],
            options={
                'ordering': ['order'],
                'unique_together': {('slug', 'stage')},
            },
        ),
    ]
