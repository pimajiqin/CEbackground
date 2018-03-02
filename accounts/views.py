# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from accounts.models import accounts
import time



def login(request):
    if request.method == "POST" and request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = accounts.objects.get(username=username)
            if user.password == password:
                response = HttpResponseRedirect("/gmce/total")
                response.set_cookie("username",username,3600)
                request.session["username"] = username+time.strftime(" %H:%M:%S")
                return response
            else:
                return HttpResponseRedirect("/accounts/login")
        except:
            return HttpResponseRedirect("/accounts/login")

    else:
        return render_to_response("accounts/login.html", locals())