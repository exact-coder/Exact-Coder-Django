# Generated by Django 4.2.6 on 2024-01-06 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_user_first_name_alter_user_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='biography',
            field=models.TextField(blank=True, max_length=800, null=True, verbose_name='User Biography'),
        ),
    ]