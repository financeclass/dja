# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-16 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmain', '0006_auto_20160816_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
