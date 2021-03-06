# Generated by Django 3.0.6 on 2020-05-17 19:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20200517_2052'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_content',
            field=models.CharField(max_length=200, verbose_name='Yorum'),
        ),
    ]
