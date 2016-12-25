# coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput
from mptt.models import MPTTModel, TreeForeignKey

# 测试用模型


@python_2_unicode_compatible
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Genre(MPTTModel):
    user = models.ForeignKey(User, null=True)
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Channel(models.Model):
    name = models.CharField(max_length=30, unique=True)
    name_en = models.CharField(max_length=30, unique=True)
    sub_channel = models.CharField(max_length=30, null=True)
    state = models.IntegerField()
    order = models.IntegerField()
    content = models.TextField(max_length=1000)
    top_url = models.URLField(null=True)
    icon = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class css_crawl(models.Model):
    name = models.CharField(max_length=30, unique=True)
    css_selector = models.CharField(max_length=200)
    url = models.URLField(null=True)
    top = models.IntegerField(null=True, blank=True)
    belong_user = models.ForeignKey(User, null=True)
    channel = models.CharField(max_length=30, null=True, blank=True)
    tags = models.CharField(max_length=30, null=True, blank=True)
    login_user = models.CharField(max_length=30, null=True, blank=True)
    login_pw = models.CharField(max_length=30, null=True, blank=True)
    include_words = models.CharField(max_length=30, null=True, blank=True)
    exclude_words = models.CharField(max_length=30, null=True, blank=True)
    error_count = models.IntegerField(null=True, blank=True)
    default_onpage = models.BooleanField(default=True)


def __str__(self):
    return self.name


@python_2_unicode_compatible
class Profile(models.Model):
    channel_chosen = models.CharField(max_length=1000, default='default')
    search_box = models.CharField(max_length=1000, default='default')
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username


@python_2_unicode_compatible
class Blog(models.Model):
    gera = models.ForeignKey(Genre, null=True)
    title = models.CharField(max_length=30)
    channel = models.CharField(max_length=30, null=True)
    folder = models.CharField(max_length=30, null=True)
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

@python_2_unicode_compatible
class Comments(models.Model):
    blog = models.ForeignKey(Blog, null=True)
    content = models.TextField(max_length=1000)
    user = models.ForeignKey(User, null=True)
    status = models.IntegerField(default=False)


    def __str__(self):
        return self.content

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'url', 'content', 'channel', 'tags', 'is_public')
        widgets = {'content': Textarea(attrs={'class': 'form-control'}),
                   'url': TextInput(attrs={'class': 'form-control'}),
                   'tags': TextInput(attrs={'class': 'form-control'}),
                   'channel': TextInput(attrs={'class': 'form-control'}),
                   'title': TextInput(attrs={'class': 'form-control'}),
                   'is_public': CheckboxInput(), }

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)

        self.fields['url'].required = False
        self.fields['content'].required = False
        self.fields['tags'].required = False
        self.fields['channel'].required = False
        self.fields['tags'].label = '标签'
        self.fields['channel'].label = '分类'
        self.fields['content'].label = '笔记'
        self.fields['url'].label = '链接'
        self.fields['title'].label = '标题'
        self.fields['is_public'].label = '是否公开'


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('channel_chosen','search_box')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['channel_chosen'].required = False
        self.fields['channel_chosen'].label = '频道选择'
        self.fields['search_box'].required = False
        self.fields['search_box'].label = '搜索设置'
