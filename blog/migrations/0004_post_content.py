# Generated by Django 3.2.12 on 2022-02-08 15:03

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default='create content', verbose_name='content'),
            preserve_default=False,
        ),
    ]
