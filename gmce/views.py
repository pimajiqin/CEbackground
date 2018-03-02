# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from gmce.functions import *
from django.http import HttpResponseRedirect
# Create your views here.



def total(request):
    """ 获取total每页30条记录，实现翻页功能 """
    try:
        request.COOKIES["username"] and request.session['username']
        username = request.COOKIES['username']

        ONE_PAGE_OF_DATA = 30
        serverall = getserverid('ceaccunt')
        try:
            curPage = int(request.GET.get('curPage', '1'))
            allPage = int(request.GET.get('allPage', '1'))
            pageType = str(request.GET.get('pageType', ''))
        except ValueError:
            curPage = 1
            allPage = 1
            pageType = ''

            # 判断点击了【下一页】还是【上一页】
        if pageType == 'pageDown':
            curPage += 1
        elif pageType == 'pageUp':
            curPage -= 1

        startPos = (curPage - 1) * ONE_PAGE_OF_DATA
        endPos = startPos + ONE_PAGE_OF_DATA
        user_list = gettotallist('ceaccunt', startPos ,endPos )

        if curPage == 1 and allPage == 1:  # 标记1
            allPostCounts = gettotalcount('ceaccunt')[0]
            allPage = allPostCounts / ONE_PAGE_OF_DATA
            remainPost = allPostCounts % ONE_PAGE_OF_DATA
            if remainPost > 0:
                allPage += 1

        return render(request, 'gmce/total.html' , {"serverall": serverall, 'user_list':user_list, 'allPage': allPage, 'curPage': curPage})
    except:
        return HttpResponseRedirect("/accounts/login")


"""
def singleinfo(request,src):

    if request.method == "POST" and request.POST:
        sid = request.POST['appname']
        sid = sid.encode("utf-8")
        int(sid)
        print type(sid)
        print sid
        serverall = getserverid('ceaccunt')
        ONE_PAGE_OF_DATA = 30
        try:
            curPage = int(request.GET.get('curPage', '1'))
            allPage = int(request.GET.get('allPage', '1'))
            pageType = str(request.GET.get('pageType', ''))
        except ValueError:
            curPage = 1
            allPage = 1
            pageType = ''

            # 判断点击了【下一页】还是【上一页】
        if pageType == 'pageDown':
            curPage += 1
        elif pageType == 'pageUp':
            curPage -= 1

        startPos = (curPage - 1) * ONE_PAGE_OF_DATA
        endPos = startPos + ONE_PAGE_OF_DATA
        # posts = BlogPost.objects.all()[startPos:endPos]
        user_list = getsingledb('ceaccunt', sid, startPos ,endPos )

        if curPage == 1 and allPage == 1:  # 标记1
            allPostCounts = getsingledbcount('ceaccunt',sid)[0]
            allPage = allPostCounts / ONE_PAGE_OF_DATA
            remainPost = allPostCounts % ONE_PAGE_OF_DATA
            if remainPost > 0:
                allPage += 1

        return render(request, 'gmce/single.html', {"serverall": serverall, 'user_list':user_list, 'allPage': allPage, 'curPage': curPage, 'sidback': sid})

    else:
        sid = 1
        serverall = getserverid('ceaccunt')
        ONE_PAGE_OF_DATA = 30
        try:
            curPage = int(request.GET.get('curPage', '1'))
            allPage = int(request.GET.get('allPage', '1'))
            pageType = str(request.GET.get('pageType', ''))
        except ValueError:
            curPage = 1
            allPage = 1
            pageType = ''

            # 判断点击了【下一页】还是【上一页】
        if pageType == 'pageDown':
            curPage += 1
        elif pageType == 'pageUp':
            curPage -= 1

        startPos = (curPage - 1) * ONE_PAGE_OF_DATA
        endPos = startPos + ONE_PAGE_OF_DATA
        # posts = BlogPost.objects.all()[startPos:endPos]
        user_list = getsingledb('ceaccunt', sid, startPos, endPos)

        if curPage == 1 and allPage == 1:  # 标记1
            allPostCounts = getsingledbcount('ceaccunt', sid)[0]
            allPage = allPostCounts / ONE_PAGE_OF_DATA
            remainPost = allPostCounts % ONE_PAGE_OF_DATA
            if remainPost > 0:
                allPage += 1

        return render(request, 'gmce/single.html',
                      {"serverall": serverall, 'user_list': user_list, 'allPage': allPage, 'curPage': curPage})
"""

def singleinfo(request,src):
    """ 获取单服统计数据 每页30条记录 """
    try:
        request.COOKIES["username"] and request.session['username']
        username = request.COOKIES['username']

        sid = src
        serverall = getserverid('ceaccunt')
        ONE_PAGE_OF_DATA = 30
        try:
            curPage = int(request.GET.get('curPage', '1'))
            allPage = int(request.GET.get('allPage', '1'))
            pageType = str(request.GET.get('pageType', ''))
        except ValueError:
            curPage = 1
            allPage = 1
            pageType = ''

            # 判断点击了【下一页】还是【上一页】
        if pageType == 'pageDown':
            curPage += 1
        elif pageType == 'pageUp':
            curPage -= 1

        startPos = (curPage - 1) * ONE_PAGE_OF_DATA
        endPos = startPos + ONE_PAGE_OF_DATA
        # posts = BlogPost.objects.all()[startPos:endPos]
        user_list = getsingledb('ceaccunt', sid, startPos, endPos)

        if curPage == 1 and allPage == 1:  # 标记1
            allPostCounts = getsingledbcount('ceaccunt', sid)[0]
            allPage = allPostCounts / ONE_PAGE_OF_DATA
            remainPost = allPostCounts % ONE_PAGE_OF_DATA
            if remainPost > 0:
                allPage += 1

        return render(request, 'gmce/single.html',
                      {"serverall": serverall, 'user_list': user_list, 'allPage': allPage, 'curPage': curPage, 'sid': sid})

    except:
        return HttpResponseRedirect("/accounts/login")




def order(request):
    """ 获取total每页30条记录，实现翻页功能 """
    try:
        request.COOKIES["username"] and request.session['username']
        username = request.COOKIES['username']

        ONE_PAGE_OF_DATA = 100
        # serverall = getserverid('ceaccunt')
        try:
            curPage = int(request.GET.get('curPage', '1'))
            allPage = int(request.GET.get('allPage', '1'))
            pageType = str(request.GET.get('pageType', ''))
        except ValueError:
            curPage = 1
            allPage = 1
            pageType = ''

            # 判断点击了【下一页】还是【上一页】
        if pageType == 'pageDown':
            curPage += 1
        elif pageType == 'pageUp':
            curPage -= 1

        startPos = (curPage - 1) * ONE_PAGE_OF_DATA
        endPos = startPos + ONE_PAGE_OF_DATA
        user_list = getorderlist('ceaccunt', startPos ,endPos )

        if curPage == 1 and allPage == 1:  # 标记1
            allPostCounts = getordercount('ceaccunt')[0]
            allPage = allPostCounts / ONE_PAGE_OF_DATA
            remainPost = allPostCounts % ONE_PAGE_OF_DATA
            if remainPost > 0:
                allPage += 1

        return render(request, 'gmce/order.html' , {'user_list':user_list, 'allPage': allPage, 'curPage': curPage})
    except:
        return HttpResponseRedirect("/accounts/login")
