import random
from copy import copy

import requests

from swiper.swiper import config


def randon_code(length=6):
    return "".join([str(random.randint(0,9)) for i in range(length)])

def send_vcode(phonenum):
    ''' 发送验证码 '''
    vcode = randon_code()
    params = copy(config.YZX_PARAMS)
    params['param'] = vcode
    params["mobile"] = phonenum
    resp = requests.post(config.YZX_API, json=params)
    print(resp.json())
    if resp.status_code is 200:
        return True
    else:
        return False

if __name__ == '__main__':
    send_vcode(17767051461)