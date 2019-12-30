'''系统状态码'''

OK = 0
SMSErr = 1000               # 发送验证码错误
VcodeExpired = 1001         # 验证码已过期
VcodeErr = 1002             # 发送验证码错误
LoginRequired = 1003        # 需要用户登录
UserDataErr = 1004          # 用户数据错误
ProfileDataErr = 1005       # 交友数据错误
ImgaeDataErr = 1006         # 图片不存在


class LogicErr(Exception):
    code = 0
    data = None

    def __init__(self, data=None):
        self.data = data or self.__class__.__name__


def gen_logic_err(name, code):
    '''产生一个异常类'''
    return type(name, (LogicErr, object), {"code": code})


SMSErr = gen_logic_err('SMSErr', 1000)                            # 发送验证码错误
VcodeExpired = gen_logic_err('VcodeExpired', 1001)                # 验证码已过期
VcodeErr = gen_logic_err('VcodeErr', 1002)                        # 发送验证码错误
LoginRequired = gen_logic_err('LoginRequired', 1003)              # 需要用户登录
UserDataErr = gen_logic_err('UserDataErr', 1004)                  # 用户数据错误
ProfileDataErr = gen_logic_err('ProfileDataErr', 1005)            # 交友数据错误
ImgaeDataErr = gen_logic_err('ImgaeDataErr', 1006)                # 图片不存在
SwipeTypeError = gen_logic_err("SwipetypeError", 1007)          # 滑动类型错误