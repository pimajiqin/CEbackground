# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class CeAccountDbInfo(models.Model):
    """ 定义账号服信息 """
    servername = models.CharField(max_length=64)
    dbname = models.CharField(max_length=64)
    ipaddr = models.GenericIPAddressField()
    dbuser = models.CharField(max_length=64)
    dbpasswd = models.CharField(max_length=64)

    def __str__(self):
        return self.servername

    class Meta:
        verbose_name_plural = "ce账号服"