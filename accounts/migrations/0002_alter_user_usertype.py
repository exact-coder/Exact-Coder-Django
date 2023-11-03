# Generated by Django 4.2.6 on 2023-11-02 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='UserType',
            field=models.CharField(choices=[('Moderator', 'Moderator'), ('User', 'User'), ('Admin', 'Admin')], default='User', max_length=100, verbose_name='User Type'),
        ),
    ]
