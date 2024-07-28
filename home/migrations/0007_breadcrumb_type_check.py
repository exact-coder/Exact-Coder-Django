# Generated by Django 5.0.6 on 2024-07-28 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_breadcrumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='breadcrumb',
            name='type_check',
            field=models.CharField(choices=[('SHOW', 'Show'), ('HIDE', 'Hide')], default='HIDE', max_length=50, verbose_name='Check Type'),
        ),
    ]