# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-12-25 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmain', '0014_auto_20161223_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='search_box',
            field=models.CharField(default='default', max_length=1000),
        ),
    ]