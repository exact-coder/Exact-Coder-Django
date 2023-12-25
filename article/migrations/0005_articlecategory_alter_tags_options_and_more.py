# Generated by Django 4.2.6 on 2023-12-23 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_alter_article_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Category Name')),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(default='Any', to='article.articlecategory'),
        ),
    ]