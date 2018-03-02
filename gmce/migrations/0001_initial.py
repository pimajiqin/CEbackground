# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-12 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CeAccountDbInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servername', models.CharField(max_length=64)),
                ('dbname', models.CharField(max_length=64)),
                ('ipaddr', models.GenericIPAddressField()),
                ('dbuser', models.CharField(max_length=64)),
                ('dbpasswd', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': 'ce\u8d26\u53f7\u670d',
            },
        ),
    ]
