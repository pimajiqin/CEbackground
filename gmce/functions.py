#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: 陈二狗


from gmce.models import CeAccountDbInfo
import MySQLdb


def gettotallist(servername, a, b):
    """ 获取账号服daily_total列表 """
    dbinfo = CeAccountDbInfo.objects.get(servername=servername)
    db = MySQLdb.connect(dbinfo.ipaddr, dbinfo.dbuser, dbinfo.dbpasswd, dbinfo.dbname)
    cursor = db.cursor()
    cursor.execute("SELECT * from daily_total order by cast(date as datetime) DESC LIMIT %d,%d;" % (a, b))
    data = cursor.fetchall()
    return data
    db.close()

def gettotalcount(servername):
    """ 获取daily_total count数 """
    dbinfo = CeAccountDbInfo.objects.get(servername=servername)
    db = MySQLdb.connect(dbinfo.ipaddr, dbinfo.dbuser, dbinfo.dbpasswd,  dbinfo.dbname)
    cursor = db.cursor()
    cursor.execute("SELECT count(*) from daily_total ;")
    data = cursor.fetchone()
    return data
    db.close()


def getsingledb(servername,serverid,a,b):
    dbinfo = CeAccountDbInfo.objects.get(servername=servername)
    db = MySQLdb.connect(dbinfo.ipaddr, dbinfo.dbuser, dbinfo.dbpasswd, dbinfo.dbname)
    cursor = db.cursor()
    cursor.execute("SELECT * from daily_total_server WHERE serverid = %s order by cast(date as datetime) DESC LIMIT %d,%d" % (serverid,a, b))
    data = cursor.fetchall()
    return data
    db.close()


def getsingledbcount(servername,serverid):
    dbinfo = CeAccountDbInfo.objects.get(servername=servername)
    db = MySQLdb.connect(dbinfo.ipaddr, dbinfo.dbuser, dbinfo.dbpasswd,  dbinfo.dbname)
    cursor = db.cursor()
    cursor.execute("SELECT count(*) from daily_total_server WHERE serverid = %s ;" % serverid)
    data = cursor.fetchone()
    return data
    db.close()

def getserverid(servername):
    dbinfo = CeAccountDbInfo.objects.get(servername=servername)
    db = MySQLdb.connect(dbinfo.ipaddr, dbinfo.dbuser, dbinfo.dbpasswd, dbinfo.dbname)
    cursor = db.cursor()
    cursor.execute("SELECT serverid,count(serverid) from daily_total_server GROUP BY serverid ORDER BY serverid DESC ;")
    data = cursor.fetchall()
    return data
    db.close()

def getordercount(servername):
    """ 获取 order_list count数 """
    dbinfo = CeAccountDbInfo.objects.get(servername=servername)
    db = MySQLdb.connect(dbinfo.ipaddr, dbinfo.dbuser, dbinfo.dbpasswd,  dbinfo.dbname)
    cursor = db.cursor()
    cursor.execute("SELECT count(*) from order_list ;")
    data = cursor.fetchone()
    return data
    db.close()

def getorderlist(servername, a, b):
    """ 获取账号服 order_list 列表 """
    dbinfo = CeAccountDbInfo.objects.get(servername=servername)
    db = MySQLdb.connect(dbinfo.ipaddr, dbinfo.dbuser, dbinfo.dbpasswd, dbinfo.dbname)
    cursor = db.cursor()
    cursor.execute("SELECT * from order_list WHERE state = 0 ORDER BY arrive_time desc LIMIT %d,%d;" % (a, b))
    data = cursor.fetchall()
    return data
    db.close()

