# Generated by Django 5.1.4 on 2024-12-28 08:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0002_alter_scholarship_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scholarship',
            name='title',
        ),
        migrations.AddField(
            model_name='scholarship',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='scholarship',
            name='applicable_program',
            field=ckeditor.fields.RichTextField(default='N/A'),
        ),
        migrations.AddField(
            model_name='scholarship',
            name='discipline',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AddField(
            model_name='scholarship',
            name='ielts',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='scholarship',
            name='location',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AddField(
            model_name='scholarship',
            name='requirement',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scholarship',
            name='scholarship_coverage',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scholarship',
            name='toefl',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]