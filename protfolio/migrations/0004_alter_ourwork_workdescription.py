# Generated by Django 4.2.6 on 2023-11-07 15:01

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protfolio', '0003_alter_ourwork_workbanner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourwork',
            name='workdescription',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Describe The Work'),
        ),
    ]
