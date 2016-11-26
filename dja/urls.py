"""dja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from appmain import views as appmain_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', appmain_views.home),
    url(r'^home/', appmain_views.home),
    url(r'^mark/', appmain_views.mark),
    url(r'^links/', appmain_views.links),
    url(r'^mylinks/', appmain_views.mylinks),
    url(r'^detail/', appmain_views.detail),
    url(r'^delete/', appmain_views.delete),
    url(r'^space/', appmain_views.space),
    url(r'^register/', appmain_views.register),
    url(r'^userlogin/', appmain_views.userlogin),
    url(r'^userlogout/', appmain_views.userlogout),
    url(r'^profileset/', appmain_views.profileset),
]
