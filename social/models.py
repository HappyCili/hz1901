from django.db import models

from common import stat


class Swiped(models.Model):
    STYPE = (
        ('like', '右滑'),
        ('superlike', '上滑'),
        ('dislike', '左滑'),
    )

    uid = models.IntegerField(verbose_name="滑动者的 ID")
    sid = models.IntegerField(verbose_name="被滑动者的 ID")
    stype = models.CharField(max_length=10, choices=STYPE, verbose_name="滑动类型")
    stime = models.DateTimeField(auto_now=True)

    @classmethod
    def swipe(cls, uid, sid, stype):
        if stype not in ['like', 'superlike', 'dislike']:
            raise stat.SwipeTypeError
        return cls.objects.get_or_create(uid=uid, sid=sid, stype=stype)

    @classmethod
    def is_like(cls, uid, sid):
        '''检测是否喜欢过某人'''
        like_types = ['like', 'superlike']
        return cls.objects.filter(uid=uid, sid=sid,
                                  stype__in=like_types).exists()
    @classmethod
    def swiped_uid_list(cls, uid):
        return Swiped.objects.filter(uid=uid).values_list("sid", flat=True)