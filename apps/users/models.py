from django.db import models


# Create your models here.


class ManageIP(models.Model):
    ip_address = models.CharField(primary_key=True, max_length=50, verbose_name='封闭地址')
    ip_status = models.BooleanField(default=False, verbose_name='封闭状态')
    ip_datetime = models.DateTimeField(auto_now=True, verbose_name='封闭时间')

    class Meta:
        verbose_name = '管理IP'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '管理IP'

