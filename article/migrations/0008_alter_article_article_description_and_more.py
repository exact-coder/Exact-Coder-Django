# Generated by Django 5.0.6 on 2024-06-28 20:01

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_alter_articlecomment_comment_article_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_description',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Article Description'),
        ),
        migrations.AlterField(
            model_name='articlesection',
            name='section_description',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Article Section Description'),
        ),
    ]
