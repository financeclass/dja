# coding:utf-8
from django import template
import re
from django.utils.http import urlquote

register = template.Library()


def mytag_link_split(value):
    return ('.').join(value.replace('http://', "").
                          replace('https://', "").replace('www.', "").replace('/', "").replace('?', "").split('.')[:2])


register.filter('mytag_link_split', mytag_link_split)


def mytag_getkey(value, para):
    return value[para]


register.filter('mytag_getkey', mytag_getkey)


def mytag_addtag(value, para):
    if value.find('tag=') == -1:
        return value + '?tag=' + urlquote(para)
    else:
        return re.sub(r'tag=([^<]+)', 'tag=' + para + '*t*' + r'\1', value)


register.filter('mytag_addtag', mytag_addtag)

# TODO: 未完成
def mytag_striptag(value ):
    return value

register.filter('mytag_striptag', mytag_striptag)