from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


# 主页视图
def index(request):
    return HttpResponse("这是BBS主页视图")


# 板块视图
def section(request, section: str):
    return HttpResponse("这是板块视图,你正在查看 " + section + " 板块")


# 帖子视图
def topic(request, topic_id: int):
    return HttpResponse("这是贴子视图," + "你正在查看帖子ID " + str(topic_id))


def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
    return render(request, 'login.html')


def userregister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        email = request.POST.get('email')
        user = User.objects.filter(username=username).first()
        if user is not None:
            info = '此账号已被注册'
            return render(request, 'register.html', {'info': info})
        else:
            User.objects.create_user(
                username=username,
                password=password
            )
            return HttpResponseRedirect('/userlogin/')
    return render(request, 'register.html')


def logout(request):
    logout(request)
    return redirect('/index/')
