# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-06 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20160628_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionalcontent',
            name='name',
            field=models.TextField(default='oName'),
            preserve_default=False,
        ),
    ]