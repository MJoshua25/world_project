# Generated by Django 2.2.5 on 2019-09-19 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_acceuil',
            field=models.BooleanField(default=False),
        ),
    ]
