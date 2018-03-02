#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: 陈二狗

""" 自定义模板过滤器 """

from django import template


register = template.Library()


@register.simple_tag
def my_tag_1(v1,v2):
    """ v1 v2 做除法运算，保留小数点2位 """
    if v1 == 0 or v2 == 0 :
        return 0
    else:
        return format(float(v1)/float(v2),'.2f')


@register.simple_tag
def my_tag_2(v1,v2):
    """ v1 v2 做除法运算，保留小数点1位，并 * 100 """
    if v1 == 0 or v2 == 0 :
        return 0
    else:
        return format(float(v1)/float(v2) * 100,'.1f')
