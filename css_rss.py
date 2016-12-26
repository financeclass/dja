# coding:utf-8

import os
from bs4 import BeautifulSoup
import urllib.request
import django
import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dja.settings")
django.setup()
from appmain.models import *
from django.contrib.auth.models import User

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

for aaa in css_crawl.objects.all():
    req = urllib.request.Request(url=aaa.url, headers=headers)
    f = urllib.request.urlopen(req).read().decode("utf8")
    soup = BeautifulSoup(f, "html.parser")
    css = ' '.join(map(lambda x: x.split('.')[0] if x.find('#') > 0 else x, aaa.css_selector.split(' ')))
    for bbb in soup.select(css):
        Blog.objects.get_or_create(title=bbb.string,url=bbb['href'],user=User.objects.get(username='admin'))
    time.sleep(123)
