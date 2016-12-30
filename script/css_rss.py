# coding:utf-8

import os
from bs4 import BeautifulSoup

import django
import time
import requests
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dja.settings")
django.setup()
from appmain.models import *
from django.contrib.auth.models import User

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
# f=requests.get('http://world.huanqiu.com/',headers=headers)
# f=f.text.encode(f.encoding)
# soup = BeautifulSoup(f, "html.parser")
# cs='html body div.wrap div.wrapCon div.conSec.marginBot40 div.imNews.bgWhite.worldNews div.listPad ul.listBoxT14 li a'
# css = ' '.join(map(lambda x: x.split('.')[0] if x.find('#') > 0 else x, cs.split(' ')))
# for aa in soup.select(css):
#     print(aa)
for aaa in css_crawl.objects.all():
    print(aaa)
    f=requests.get(aaa.url,headers=headers)
    f=f.text.encode(f.encoding)

    soup = BeautifulSoup(f, "html.parser")
    css = ' '.join(map(lambda x: x.split('.')[0] if x.find('#') > 0 else x, aaa.css_selector.split(' ')))
    for bbb in soup.select(css):
        Blog.objects.get_or_create(title=bbb.string,url=bbb['href'],user=User.objects.get(username='admin'))

    time.sleep(1)
