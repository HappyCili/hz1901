import os

from django.core.cache import cache
from django.utils import datastructures

from user.models import User
from user import logics
from user.forms import UserForm, ProfileForm
from common import stat, keys
from lib.http import render_json
from lib.orm import model_to_dict
from lib.qncloud import upload_to_qn


def get_vcode(request):
    ''' 用户获取验证码'''
    phonenum = request.GET.get("phonenum")
    if logics.send_vcode(phonenum):
        return render_json(code=stat.OK)
    else:
        raise stat.SMSErr


def check_vcode(request):
    '''检查验证码， 并进行登录注册'''
    phonenum = request.POST.get("phonenum")
    vcode = request.POST.get("vcode")
    cache_vcode = cache.get(keys.VCODE_KEY % phonenum)
    # 检测验证码是否过期
    if cache_vcode is None:
       raise stat.VcodeExpired
    # 判断验证码是否一致
    if cache_vcode == vcode:
        try:
            user = User.objects.get(phonenum=phonenum)
        except User.DoesNotExist:
            user = User.objects.create(phonenum=phonenum, nickname=phonenum)
        # 使用session记录登录状态
        request.session['uid'] = user.id
        return render_json(code=0, data=user.to_dict())
    else:
        raise stat.VcodeErr


def get_profile(request):
    '''获取个人资料'''
    print(request.META)
    profile = request.user.profile
    return render_json(model_to_dict(profile))


def set_profile(request):
    '''修改个人信息,及交友资料'''
    user = request.user
    user_form = UserForm(request.POST)
    if user_form.is_valid():
        user.__dict__.update(user_form.cleaned_data)    # 更新兑现属性
        user.save()
    else:
        raise stat.UserDataErr(user_form.errors)
    profile_form = ProfileForm(request.POST)
    if profile_form.is_valid():
        profile = profile_form.save(commit=False)
        profile.id = user.id
        profile.save()
    else:
        raise stat.ProfileDataErr(profile_form.errors)
    return render_json()


def upload_avatar(request):
    '''上传头像'''
    try:
        avatar_file = request.FILES['avatar']
    except datastructures.MultiValueDictKeyError:
        raise stat.ImgaeDataErr
    logics.upload_avatar.delay(request.user, avatar_file)
    return render_json()
