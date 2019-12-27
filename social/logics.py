import datetime

from user.models import User


def rcmd(user):
    today = datetime.date.today()
    max_birthday = today - datetime.tiemdelta(user.profile.min_dating_age * 365)
    min_birthday = today - datetime.tiemdelta(user.profile.max_dating_age * 365)
    users = User.objects.filter(
        sex=user.profile.dating_sex,
        location=user.profile.dating_location,
        birthday__lte=max_birthday,
        birthday__gte=min_birthday,
    )[:20]

    # TODO: 需要排除已划过的用户
    return users