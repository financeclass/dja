# coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.forms import ModelForm

# 测试用模型
@python_2_unicode_compatible
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Profile(models.Model):
    channel_chosen = models.CharField(max_length=1000, default='default')
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username


@python_2_unicode_compatible
class Blog(models.Model):
    title = models.CharField(max_length=30)
    channel = models.CharField(max_length=30, null=True)
    on_page = models.BooleanField(default=False)
    editor = models.ForeignKey(User, null=True, related_name='blog_editor')
    tags = models.CharField(max_length=30, null=True)
    content = models.TextField(max_length=1000)
    user = models.ForeignKey(User, null=True)
    url = models.URLField(null=True)
    is_public = models.BooleanField(default=False)
    from_link = models.ForeignKey('self', null=True)
    republish = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'url', 'content', 'tags', 'is_public')

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['url'].required = False
        self.fields['content'].required = False
        self.fields['tags'].required = False
        self.fields['tags'].label = '标签'
        self.fields['content'].label = '笔记'
        self.fields['url'].label = '链接'
        self.fields['title'].label = '标题'
        self.fields['is_public'].label = '是否公开'


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('channel_chosen',)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['channel_chosen'].required = False
        self.fields['channel_chosen'].label = '频道选择'
