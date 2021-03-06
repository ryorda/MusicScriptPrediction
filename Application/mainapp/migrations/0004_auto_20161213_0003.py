# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-13 00:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20161212_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=48, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='song',
            name='year',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
