import datetime


from user.models import User
from social.models import Swiped


def rcmd(user):
    today = datetime.date.today()
    max_birthday = today - datetime.tiemdelta(user.profile.min_dating_age * 365)
    min_birthday = today - datetime.tiemdelta(user.profile.max_dating_age * 365)
    swiped_ids = Swiped.swiped_uid_list(user.id)
    users = User.objects.filter(
        sex=user.profile.dating_sex,
        location=user.profile.dating_location,
        birthday__lte=max_birthday,
        birthday__gte=min_birthday,
    ).exclude(id__in=swiped_ids)[:20]
    return users


def like_someone(user, sid):
    '''喜欢某人'''
    Swiped.swipe(user.id, sid, 'like')
    # 检查对方是否喜欢过自己
    if Swiped.is_like(sid, user.uid):
        # TODO: 匹配好友关系
        return True
    else:
        return False