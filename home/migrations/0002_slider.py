# Generated by Django 4.2.6 on 2024-01-09 14:26

import autoslug.fields
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_title', models.CharField(max_length=250, verbose_name='Slider Title')),
                ('slider_subtitle', models.CharField(blank=True, max_length=200, null=True, verbose_name='Slider Subtitle')),
                ('slider_image', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, quality=-1, scale=None, size=[1500, 800], upload_to='slider/', verbose_name='Slider Image')),
                ('slider_type', models.CharField(blank=True, max_length=20, null=True, verbose_name='Slider Type')),
                ('button_text', models.CharField(max_length=20, verbose_name='Action Button Text')),
                ('button_link', models.URLField(blank=True, null=True, verbose_name='URL of Redirect Page')),
                ('show_or_hide', models.CharField(choices=[('SHOW', 'Show'), ('HIDE', 'Hide')], default='HIDE', max_length=50, verbose_name='Show or Hide')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='slider_title', unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
        ),
    ]
