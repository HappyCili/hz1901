import datetime

from django.db import models

# Create your models here.

class User(models.Model):
    SEX = (
        ('male', "男性"),
        ('femal', "女性"),
    )
    LOCATION = (
        ('北京', '北京'),
        ('上海', '上海'),
        ('广州', '广州'),
        ('深圳', '深圳'),
        ('杭州', '杭州'),
        ('武汉', '武汉'),
        ('成都', '成都'),
    )
    phonenum = models.CharField(max_length=16, unique=True, verbose_name="手机号")
    nickname = models.CharField(max_length=16, verbose_name="昵称")
    sex = models.CharField(max_length=8, choices=SEX, verbose_name="性别")
    birthday = models.Field(default=datetime.date(1990,1,1), verbose_name="出生日")
    avatar = models.CharField(max_length=256, verbose_name="个人形象")
    location  = models.CharField(max_length=16, choices=LOCATION, verbose_name="常居地")