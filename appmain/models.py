# coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.forms import ModelForm

@python_2_unicode_compatible
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Blog(models.Model):
    title = models.CharField(max_length=30)
    channel = models.CharField(max_length=30,null=True)
    tags = models.CharField(max_length=30,null=True)
    content = models.TextField(max_length=1000)
    user = models.ForeignKey(User,null=True)
    url=models.URLField(null=True)
    type = models.IntegerField(null=True)
    is_public=models.BooleanField(default=False)

    def __str__(self):
        return self.title

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'url', 'content','channel','is_public')
    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['url'].required = False
        self.fields['content'].required = False
        self.fields['channel'].required = False
        self.fields['channel'].label = '分类'
        self.fields['content'].label = '笔记'
        self.fields['url'].label = '链接'
        self.fields['title'].label = '标题'