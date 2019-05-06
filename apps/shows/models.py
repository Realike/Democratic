from django.db import models

# Create your models here.


class Content(models.Model):
    content_text = models.CharField(max_length=200, verbose_name='发布内容')
    content_image = models.ImageField(max_length=100, null=True, verbose_name='发布图片')
    content_date = models.DateTimeField(auto_now=True, verbose_name='发布日期')
    content_yes = models.IntegerField(default=0, verbose_name='支持')
    content_no = models.IntegerField(default=0, verbose_name='反对')

    class Meta:
        verbose_name = '发布内容'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content_text
