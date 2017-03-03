# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-03 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_name', models.CharField(max_length=50, verbose_name='\u8d44\u4ea7\u540d\u79f0')),
                ('idc_id', models.IntegerField(verbose_name='idc\u7f16\u53f7')),
                ('ipaddr', models.CharField(max_length=15, verbose_name='IP\u5730\u5740')),
                ('cabinet_num', models.CharField(max_length=20, verbose_name='\u673a\u67dc\u7f16\u53f7')),
                ('run_service', models.CharField(max_length=50, verbose_name='\u8fd0\u884c\u670d\u52a1')),
                ('listen_port', models.CharField(max_length=50, verbose_name='\u76d1\u542c\u7aef\u53e3')),
                ('service_fact', models.CharField(max_length=50, verbose_name='\u670d\u52a1\u5668\u5382\u5bb6')),
                ('asset_memory', models.SmallIntegerField(verbose_name='\u8d44\u4ea7\u5185\u5b58')),
                ('cpu_type', models.SmallIntegerField(verbose_name='cpu\u578b\u53f7')),
                ('cpu_num', models.SmallIntegerField(verbose_name='\u7269\u7406cpu\u6570\u91cf')),
                ('hard_disk', models.CharField(max_length=20, verbose_name='\u786c\u76d8')),
                ('hostname', models.CharField(max_length=20, verbose_name='\u4e3b\u673a\u540d')),
                ('os_type', models.CharField(max_length=20, verbose_name='\u64cd\u4f5c\u7cfb\u7edf')),
                ('sn', models.CharField(max_length=20, verbose_name='\u5feb\u901f\u670d\u52a1\u7f16\u7801')),
                ('mac', models.CharField(max_length=48, verbose_name='mac\u5730\u5740')),
                ('ground_date', models.DateTimeField(verbose_name='\u4e0a\u67b6\u65f6\u95f4')),
            ],
        ),
    ]