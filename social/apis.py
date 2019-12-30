
from lib.http import render_json
from social import logics

def rcmd_users(request):
    '''获取推荐列表'''
    users = logics.rcmd(request.user)
    result = [user.to_dict for user in users]
    return render_json(result)


def like(request):
    '''喜欢'''
    sid = request.POST.get("sid")
    is_matched = logics.like_someone(request.user, sid)
    return render_json(data={'is_matched': is_matched})


def superlike(request):
    '''超级喜欢'''
    return render_json()


def rewind(request):
    '''反悔'''
    return render_json()


def show_liked_me(request):
    '''查看喜欢过我的人'''
    return render_json()


def friend_list(request):
    '''查看好友列表'''
    return render_json()



