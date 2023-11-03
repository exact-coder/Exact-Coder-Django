# Generated by Django 4.2.6 on 2023-11-02 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='UserType',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Moderator', 'Moderator'), ('User', 'User')], default='User', max_length=100, verbose_name='User Type'),
        ),
    ]
