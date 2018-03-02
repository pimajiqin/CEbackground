#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: 陈二狗

from django.conf.urls import include, url
from django.contrib import admin
from accounts import views as accounts_views

urlpatterns = [
    url(r'login/$', accounts_views.login),
]