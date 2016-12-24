# coding:utf-8
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from functools import reduce

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')


default_channel = [u'电影', u'音乐', u'小说', u'编程', ]

icon_dict = {u'电影': 'film', u'音乐': 'music', u'小说': 'pencil-square', u'编程': 'code'}


def index(request):
    return HttpResponse(u"welcome!  欢迎光临!")


@login_required(login_url="/userlogin/")
def create_folder(request):
    if request.method == 'POST':

        new_folder = Genre.objects.create(user=request.user,
                                  name=request.POST.get('folder_name', None),
                                  parent=Genre.objects.get(id=request.GET.get('folder', None)))
        return HttpResponseRedirect("/mylinks/")
    else:
        return render(request, 'appmain/create_folder.html', locals())


@login_required(login_url="/userlogin/")
def mylinks(request):
    if request.GET.get('folder', None) is None:
        folder_now = Genre.objects.get_or_create(user=request.user, name='root123')[0]
        linklist = Blog.objects.filter(user=request.user).order_by('-id')
        linklist = linklist.filter(Q(gera__isnull=True) | Q(gera=folder_now)).order_by('-id')
    else:
        folder_now = Genre.objects.get(id=request.GET.get('folder', None))
        linklist = Blog.objects.filter(user=request.user).order_by('-id')
        if folder_now.parent_id:

            linklist = linklist.filter(gera=folder_now).order_by('-id')
        else:
            linklist = linklist.filter(Q(gera__isnull=True) | Q(gera=folder_now)).order_by('-id')

    folders = Genre.objects.filter(parent=folder_now).order_by('name')

    page = int(request.GET.get('page', 1))

    # ----------tag 处理开始---------------
    # if linklist.count()>0:
    # if request.GET.get('tag', None) is not None:
    #         query_tag_list = request.GET.get('tag').split('*t*')
    #         for aaa in query_tag_list:
    #             linklist = linklist.filter(tags__contains=aaa)
    #
    #     tagset = set(reduce(lambda x, y: x + y, linklist.values_list('tags')))
    #     if None in tagset:
    #         tagset.remove(None)
    #     if '' in tagset:
    #         tagset.remove('')
    #     tags = set(reduce(lambda x, y: str(x) + ',' + str(y), tagset).replace(u'，',',').split(','))
    #     if request.GET.get('tag', None) is not None:
    #         for aaa in request.GET.get('tag').split('*t*'):
    #             tags.remove(aaa)
    # ----------tag 处理结束---------------
    thetype = 'mylinks'
    linklist = linklist[page * 5 - 5:page * 5]
    return render(request, 'appmain/links.html', locals())


def home(request):
    channellist_local = [{'channel_name': aaa, 'channel_icon': icon_dict.get(aaa, 'angle-down')}
                         for aaa in default_channel]
    linklist = [['1']]
    if request.user.is_authenticated():
        try:
            userchannel = Profile.objects.get(user=request.user).channel_chosen
            if userchannel != 'default':
                userchannel_list = userchannel.replace('，', ',').split(',')
                channellist_local = [{'channel_name': aaa, 'channel_icon': icon_dict.get(aaa, 'angle-down')}
                                     for aaa in userchannel_list]
        except Exception as e:
            pass
        hasfav = Blog.objects.filter(user=request.user).values_list('from_link')
        hasfav = [aaa[0] for aaa in hasfav]

    for aa in channellist_local:
        linklist.append(
            [aa, Blog.objects.filter(channel=aa['channel_name']).filter(is_public=True).order_by('-id')[:4]])
    linklist.append([{'channel_name': 'other', 'channel_icon': 'angle-down'},
                     Blog.objects.exclude(channel__in=[aaa['channel_name'] for aaa in channellist_local]).filter(
                         is_public=True).order_by('-id')[:4]])

    return render(request, 'appmain/home.html', locals())


def detail(request):
    if request.user.is_authenticated():
        hasfav = Blog.objects.filter(user=request.user).values_list('from_link')
        hasfav = [aaa[0] for aaa in hasfav]
    link = get_object_or_404(Blog, id=request.GET.get('linkid', 0))
    if link.user != request.user and link.is_public == False:
        return HttpResponse(u"无权限")
    return render(request, 'appmain/detail.html', locals())


def links(request):
    page = int(request.GET.get('page', 1))
    if request.user.is_authenticated():
        hasfav = Blog.objects.filter(user=request.user).values_list('from_link')
        hasfav = [aaa[0] for aaa in hasfav]
    if request.GET.get('channel', None) == 'other':
        linklist = Blog.objects.exclude(channel__in=default_channel).filter(is_public=True).order_by('-id')
    else:
        linklist = Blog.objects.filter(channel=request.GET.get('channel', None)).filter(is_public=True).order_by(
            '-id')
    linklist = linklist[page * 5 - 5:page * 5]
    thetype = 'links'
    return render(request, 'appmain/links.html', locals())


@login_required(login_url="/userlogin/")
def mark(request):
    # TODO: 补全http
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            if int(request.GET.get('edit', 0)) == 0:
                newblog = Blog.objects.create(title=form.cleaned_data['title'],
                                              tags=form.cleaned_data['tags'],
                                              channel=form.cleaned_data['channel'],
                                              content=form.cleaned_data['content'],
                                              url=form.cleaned_data['url'],
                                              is_public=form.cleaned_data['is_public'],
                                              user=request.user)
                if int(request.GET.get('linkid', 0)) > 0:
                    Blog.objects.filter(id=newblog.id).update(from_link=
                                                              Blog.objects.get(id=request.GET.get('linkid', 0)))
                if int(request.GET.get('folder', 0)) > 0:
                    Blog.objects.filter(id=newblog.id).update(
                        gera=Genre.objects.get(id=request.GET.get('folder', None)))
            else:
                Blog.objects.filter(id=request.GET.get('linkid', 0),
                                    user=request.user).update(title=form.cleaned_data['title'],
                                                              tags=form.cleaned_data['tags'],
                                                              channel=form.cleaned_data['channel'],
                                                              content=form.cleaned_data['content'],
                                                              is_public=form.cleaned_data['is_public'],
                                                              url=form.cleaned_data['url'])

        return HttpResponseRedirect("/mylinks/")
    elif int(request.GET.get('linkid', 0)) > 0:
        thebolg = Blog.objects.get(id=request.GET.get('linkid', 0))
        form = BlogForm(instance=thebolg)
        return render(request, 'appmain/mark.html', locals())
    else:
        form = BlogForm()
        return render(request, 'appmain/mark.html', locals())


@login_required(login_url="/userlogin/")
def delete(request):
    Blog.objects.filter(id=request.GET.get('linkid', None), user=request.user).delete()
    return HttpResponseRedirect("/mylinks/")


@login_required(login_url="/userlogin/")
def space(request):
    return render(request, 'appmain/space.html', locals())


@login_required(login_url="/userlogin/")
def profileset(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            Profile.objects.filter(user=request.user).update(channel_chosen=form.cleaned_data['channel_chosen'])
            return HttpResponseRedirect("/space/")
    else:
        form = ProfileForm(instance=Profile.objects.get_or_create(user=request.user)[0])
        return render(request, 'appmain/mark.html', locals())


# --------------- register ------------------

def register(request):
    if request.method == 'POST':
        try:
            User.objects.create(username=request.POST.get('username', None), is_staff=True)
            u = User.objects.get(username=request.POST.get('username', None))
            Profile.objects.get_or_create(user=u)
            u.set_password(request.POST.get('password', None))
            u.save()
            login(request, authenticate(username=request.POST.get('username', None),
                                        password=request.POST.get('password', None)))
            return HttpResponseRedirect("/home/")
        except Exception as e:
            error_msg = '用户名已占用'
            return render(request, 'appmain/register.html', locals())

    else:
        return render(request, 'appmain/register.html', locals())


def userlogin(request):
    if request.method == 'POST':
        auth = authenticate(username=request.POST.get('username', None),
                            password=request.POST.get('password', None))
        if auth is not None:
            login(request, auth)
            # todo: login next 无效
            return HttpResponseRedirect('/home/')
        else:
            return render(request, 'appmain/login.html', {'error_msg': '用户不存在或密码错误'})
    else:
        return render(request, 'appmain/login.html')


def userlogout(request):
    logout(request)
    return HttpResponseRedirect("/home/")


