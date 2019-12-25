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
    location = models.CharField(max_length=16, choices=LOCATION, verbose_name="常居地")

    @property
    def profile(self):
        '''用户的交友资料'''
        if not hasattr(self,'_profile'):
            self._profile, _ = Profile.objects.get_or_create(id=self.id)
        return self._profile

    def to_dict(self):
        return {
            'id': self.id,
            'phonenum' : self.phonenum,
            'nickname' : self.nickname,
            'sex' : self.sex,
            'birthday' : self.birthday,
            'avatar' : self.avatar,
            'location' : self.location,
        }


class Profile(models.Model):
    dating_sex = models.CharField(max_length=8, choices=User.SEX, verbose_name='匹配的性别')
    dating_location = models.CharField(max_length=16, choices=User.LOCATION, verbose_name='目标城市')
    min_distance = models.IntegerField(default=1, verbose_name='最小查找范围')
    max_distance = models.IntegerField(default=10, verbose_name='最大查找范围')
    min_dating_age = models.IntegerField(default=18, verbose_name='最小交友年龄')
    max_dating_age = models.IntegerField(default=50, verbose_name='最大交友年龄')
    vibration = models.BooleanField(verbose_name='开启震动')
    only_matche = models.BooleanField(verbose_name='不让为匹配的人看我的相册')
    auto_play = models.BooleanField(verbose_name='是否自动播放视频')

    def to_dict(self):
        return {
            'dating_sex': self.dating_sex,
            'dating_locatio': self.dating_locatio,
            'min_distance': self.min_distance,
            'max_distance': self.max_distance,
            'min_dating_age': self.min_dating_age,
            'max_dating_age': self.max_dating_age,
            'vibration': self.vibration,
            'only_matche': self.only_matche,
            'auto_play': self.auto_play,
        }