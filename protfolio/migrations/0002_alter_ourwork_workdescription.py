# Generated by Django 5.0.6 on 2024-06-28 20:01

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourwork',
            name='workdescription',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Describe The Work'),
        ),
    ]
