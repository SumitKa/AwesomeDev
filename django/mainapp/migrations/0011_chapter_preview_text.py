# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-11 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_chapter_preview_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='preview_text',
            field=models.CharField(default=42, max_length=300),
            preserve_default=False,
        ),
    ]
