# Generated by Django 2.1.8 on 2019-05-05 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_text', models.CharField(max_length=200, verbose_name='发布内容')),
                ('content_image', models.ImageField(null=True, upload_to='', verbose_name='发布图片')),
                ('content_date', models.DateTimeField(auto_now=True, verbose_name='发布日期')),
                ('content_yes', models.IntegerField(default=0, verbose_name='支持')),
                ('content_no', models.IntegerField(default=0, verbose_name='反对')),
            ],
            options={
                'verbose_name': '发布内容',
                'verbose_name_plural': '发布内容',
            },
        ),
    ]
