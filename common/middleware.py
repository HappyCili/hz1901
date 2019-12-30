from django.utils.deprecation import MiddlewareMixin

from lib.http import render_json
from user.models import User
from common import stat


class AuthMiddleware(MiddlewareMixin):
    PATH_WHITE_LIST = [
        '/api/uesr/get_vcode',
        '/api/uesr/check_vcode'
    ]

    def process_request(self, request):
        # 检测当前访问的路径是否在白名单中
        if request.path in self.PATH_WHITE_LIST:
            return
        uid = request.session.get('uid')
        # session中是否已存在uid
        if not uid:
            return render_json(code=stat.LoginRequired, data='LoginRequired')
        # 获取当前用户
        request.user = User.objects.get(id=uid)

class LogicErrMiddleware(MiddlewareMixin):

    def process_exception(self, request, exception):
        if isinstance(exception, stat.LogicErr):
            return render_json(data=exception.data, code=exception.code)