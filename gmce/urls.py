#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: 陈二狗
from django.conf.urls import url
from gmce import views as gmce_views

urlpatterns = [
    url(r'total/$', gmce_views.total, name="gmce_total"),
    url(r'order/$', gmce_views.order, name="gmce_order"),
    url(r'single/(\w+)', gmce_views.singleinfo),
]