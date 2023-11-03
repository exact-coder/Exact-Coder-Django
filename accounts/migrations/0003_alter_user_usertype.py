# Generated by Django 4.2.6 on 2023-11-03 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_administration_moderator_reader_alter_user_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='UserType',
            field=models.CharField(choices=[('ADMINISTRATION', 'Administration'), ('MODERATOR', 'Moderator'), ('READER', 'Reader')], default='ADMINISTRATION', max_length=100, verbose_name='User Type'),
        ),
    ]
