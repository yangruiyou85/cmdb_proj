# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Asset(models.Model):
    asset_name = models.CharField(max_length=50, verbose_name='资产名称')
    ipaddr = models.GenericIPAddressField('IP地址')
    cabinet_num = models.CharField('机柜编号', max_length=20)
    run_service = models.CharField('运行服务', max_length=50)
    listen_port = models.CharField('监听端口', max_length=50)
    service_fact = models.CharField('服务器厂家', max_length=50)
    asset_memory = models.SmallIntegerField('资产内存', null=True)
    cpu_type = models.SmallIntegerField(verbose_name='cpu型号', null=True)
    cpu_num = models.SmallIntegerField('物理cpu数量', null=True)
    hard_disk = models.CharField('硬盘', max_length=20, null=True)
    hostname = models.CharField('主机名', max_length=20, null=True)
    os_type = models.CharField('操作系统', max_length=20, null=True)
    sn = models.CharField('快速服务编码', max_length=20, null=True)
    mac = models.CharField('mac地址', max_length=48, null=True)
    ground_date = models.DateTimeField('上架时间')


class Maintains(models.Model):
    record = models.CharField('维护记录', max_length=200)
    comments = models.CharField('备注', max_length=100)
    maintain_date = models.DateTimeField('维护时间')


class Ribao(models.Model):
    ribao_type = models.CharField('日报类型', max_length=50)
    work_date = models.DateTimeField('工作时间')
    work_content = models.CharField('工作内容', max_length=500)
    use_time = models.SmallIntegerField('工作时长')
    solve = models.CharField('解决方法', max_length=50)
    commit_date = models.DateTimeField('提交时间')


class Users(models.Model):
    username = models.CharField('用户名', max_length=50)
    realname = models.CharField('姓名', max_length=50)
    user_passwd = models.CharField('登陆密码', max_length=50)
    phone = models.CharField('电话号码', max_length=11)
    email = models.EmailField('电子邮件')
    isactive = models.BooleanField('是否激活')
    reg_date = models.DateTimeField('注册时间')
    last_login_date = models.DateTimeField('最后登录时间')


class Roles(models.Model):
    role_name = models.CharField('角色名', max_length=50)
    role_realname = models.CharField('角色实名', max_length=50)
    comments = models.CharField('备注', max_length=50)


class Idc(models.Model):
    idc_name = models.CharField('idc名称', max_length=20)
    idc_phone = models.CharField('idc联系人电话', max_length=11)
    idc_username = models.CharField('idc联系人', max_length=50)
    idc_addr = models.CharField('idc地址', max_length=50, null=True)
    comments = models.CharField('备注', null=True, max_length=100)
    update_date = models.DateTimeField('更新时间', null=True)
