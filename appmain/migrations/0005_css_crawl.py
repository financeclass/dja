# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-12-02 14:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appmain', '0004_blog_republish'),
    ]

    operations = [
        migrations.CreateModel(
            name='css_crawl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('css_selector', models.CharField(max_length=30)),
                ('url', models.URLField(null=True)),
                ('top', models.IntegerField(null=True)),
                ('channel', models.CharField(max_length=30, null=True)),
                ('tags', models.CharField(max_length=30, null=True)),
                ('belong_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]