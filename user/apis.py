import random

from django.http import JsonResponse
from django.core.cache import cache

from swiper.user.models import User
from swiper.user import logics
from swiper.common import stat, keys
from swiper.lib.http import render_json

def get_vcode(request):
    ''' 用户获取验证码'''
    phonenum = request.GET.get("phonenum")
    if logics.send_vcode(phonenum):
        return render_json(code=stat.OK, data=None)
    else:
        return render_json(code=stat.SMSErr, data="SMSError")

def check_vcode(request):
    '''检查验证码， 并进行登录注册'''
    phonenum = request.POST.get("phonenum")
    vcode = request.POST.get("vcode")
    cache_vcode = cache.get(keys.VCODE_KEY % phonenum)
    # 检测验证码是否过期
    if cache_vcode is None:
        return render_json(code=stat.VcodeExpired, data="VcodeExpired")
    # 判断验证码是否一致
    if cache_vcode == vcode:
        try:
            user = User.objects.get(phonenum=phonenum)
        except User.DoesNOtExist:
            user = User.objects.create(phonenum=phonenum, nickname=phonenum)
        # 使用session记录登录状态
        request.session['uid'] = user.id
        return render_json(code=0, data=user.to_dict())
    else:
        return render_json(code=stat.VcodeErr, data="VcodeError")
