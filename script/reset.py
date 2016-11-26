#!/usr/bin/env python
# coding:utf-8

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zbyd.settings")

'''
Django 版本大于等于1.7的时候，需要加上下面两句
import django
django.setup()
否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
'''

import django

if django.VERSION >= (1, 7):
    django.setup()

from mainapp.models import *
from threadedcomments.models import *
from django.contrib.auth.models import User


def main():
    user = User()
    user.username = '管理员'
    user.set_password('1234qwer')
    user.is_superuser = True
    user.is_active = True
    user.is_staff = True
    user.save()
    user = User()
    user.username = '用户1'
    user.set_password('1234qwer')
    user.is_active = True
    user.save()
    user = User()
    user.username = '用户2'
    user.set_password('1234qwer')
    user.is_active = True
    user.save()

    cate.objects.create(catename1='film')
    cate.objects.create(catename1='code')

    link.objects.create(user=User.objects.get(username='管理员'),
                        belongcate=cate.objects.get(catename1='film'),
                        linkname='这是一个示例链接',
                        url='http://movie.douban.com/subject/6307447/',
                        abstract='这里是简介 ')
    link.objects.create(user=User.objects.get(username='管理员'),
                        belongcate=cate.objects.get(catename1='film'),
                        linkname='这还是示例链接',
                        url='http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000',
                        abstract='这里是简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介简介 ')
    link.objects.create(user=User.objects.get(username='用户1'),
                        belongcate=cate.objects.get(catename1='film'),
                        linkname='又一个示例链接',
                        url='https://www.djangoproject.com/',
                        abstract='''这里是简介这里是简介这里是简介这里是简介这里是简介这里是简介
                                 这里是简介这里是简介这里是简介这里是简介这里是简介这里是简介
                                 这里是简介这里是简介这里这里是简介这里是简介这里这里是简介
                                 这里是简介这里这里是简介这里是简介这里''')
    link.objects.create(user=User.objects.get(username='用户2'),
                        belongcate=cate.objects.get(catename1='code'),
                        linkname='第三个示例链接',
                        url='http://www.ziqiangxuetang.com/django/django-tutorial.html',
                        abstract='这里是简介这里是简介这里是简介这里是简介这里是简介这里是简介')

    Person.objects.create(name=User.objects.get(username='管理员'),
                          age=1,
                          link=link.objects.filter(user=User.objects.get(username='管理员'))[0], )


if __name__ == "__main__":
    main()
    print('Done!')