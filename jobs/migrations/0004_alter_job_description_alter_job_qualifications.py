# Generated by Django 5.1.4 on 2024-12-27 11:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_job_options_job_benefits_job_company_logo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='qualifications',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
