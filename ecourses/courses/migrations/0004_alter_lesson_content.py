# Generated by Django 5.0.4 on 2024-05-03 03:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_tag_lesson_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]