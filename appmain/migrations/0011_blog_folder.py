# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-12-17 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmain', '0010_channel'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='folder',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
