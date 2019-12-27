import os
import random
from copy import copy
from django.core.cache import cache

from lib.http import render_json
from lib.qncloud import upload_to_qn
from swiper import settings
from swiper import config
from common import keys

from workon import celery_app

def random_code(length=6):
    return "".join([str(random.randint(0,9)) for i in range(length)])


def send_vcode(phonenum):
    ''' 发送验证码 '''
    # vcode = random_code()
    vcode = "1111"
    cache.set(keys.VCODE_KEY % phonenum, vcode, 1800000) # 使用缓存记录验证码，时间到了自动过期
    print(keys.VCODE_KEY % phonenum)
    params = copy(config.YZX_PARAMS)
    params['param'] = vcode
    params["mobile"] = phonenum
    return True
    # resp = requests.post(config.YZX_API, json=params)
    # print(resp.json())
    # if resp.status_code is 200:
    #     return True
    # else:
    #     return False


def save_avatar(uplpad_file, uid):
    filename = "Avatar-%s" %uid
    fullpath = os.path.join(settings.MEDIA_ROOT, filename)
    print(fullpath)
    with open(fullpath, "wb") as fp:
        for chunk in uplpad_file.chunks():
            fp.write(chunk)
    return fullpath, filename


@celery_app.task
def upload_avatar(user, avatar_file):
    """上传头像"""
    # 将文件保存到服务器
    fullpath, filename = save_avatar(avatar_file, user.id)
    # 上传到七牛云
    file_url = upload_to_qn(fullpath, filename)
    # 删除本地文件
    os.remove(fullpath)
    # 将链接保存到数据库
    user.avatar = file_url
    user.save()