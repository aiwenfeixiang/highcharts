from django.db import models

from django.db import models


class Depart(models.Model):
    """ 部门表 """
    title = models.CharField(verbose_name='部门', max_length=32)


class Server(models.Model):
    """ 服务器 """
    hostname = models.CharField(verbose_name='主机名', max_length=32)
    depart = models.ForeignKey(verbose_name='部门', to='Depart')
