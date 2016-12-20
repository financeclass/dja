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


def parse_url(url, para, value):
    url_list = url.split('/?')
    if len(url_list) == 1:
        return url
    else:
        para_list = url_list[1].split('&')
        for index, aaa in enumerate(para_list):
            if aaa.split('=')[0] == para:
                para_list[index] = para + '=' + value
        return url_list[0] + '/?' + '&'.join(para_list)


def previous_page(value, para):
    if value.find('/?') == -1:
        value += '/?page=1'
    elif value.find('page=') == -1:
        value += '&page=1'
    return parse_url(value, 'page', str(para - 1))


register.filter('previous_page', previous_page)


def next_page(value, para):
    if value.find('/?') == -1:
        value += '/?page=1'
    elif value.find('page=') == -1:
        value += '&page=1'
    return parse_url(value, 'page', str(para + 1))


register.filter('next_page', next_page)


def mytag_addtag(value, para):
    if value.find('tag=') == -1:
        return value + '?tag=' + urlquote(para)
    else:
        return re.sub(r'tag=([^<]+)', 'tag=' + para + '*t*' + r'\1', value)


register.filter('mytag_addtag', mytag_addtag)

# TODO: 未完成
def mytag_striptag(value):
    return value


register.filter('mytag_striptag', mytag_striptag)