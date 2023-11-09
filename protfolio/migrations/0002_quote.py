# Generated by Django 4.2.6 on 2023-11-09 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_date_joined'),
        ('protfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeQuote', models.TextField(max_length=200, verbose_name='Write Your Quote in short')),
                ('employeeUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.employee', verbose_name='Employee User')),
            ],
        ),
    ]
