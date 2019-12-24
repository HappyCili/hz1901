import random

from django.http import JsonResponse
from swiper.swiper import config
from .logics import send_vcode
from swiper.common import stat


def get_vcode(request):
    ''' 用户获取验证码'''
    phonenum = request.GET.get("phonenum")
    if send_vcode(phonenum):
        return JsonResponse({'code': stat.OK, "data": None})
    else:
        return JsonResponse({'code': stat.VcodeErr, "data": "VcodeError"})

def check_vcode(request):
    phonenum = request.POST.get("phonenum")
    vcode = request.POST.get("vcode")
    return JsonResponse({})