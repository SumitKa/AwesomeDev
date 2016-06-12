# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-10 09:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('video_url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('video_url', models.CharField(max_length=255)),
                ('start_time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pictures_array', models.CharField(max_length=255)),
                ('textblocks_array', models.CharField(max_length=1000)),
                ('additional_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.AdditionalContent')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('twitter_account', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Person'),
        ),
        migrations.AddField(
            model_name='additionalcontent',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Chapter'),
        ),
    ]