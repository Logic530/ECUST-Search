#-*- coding:utf-8 -*-
from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
import json
from django.contrib.auth.models import User
from bbs.form import UserForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from ecust_search.settings import EMAIL_FROM
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","ecust_search.settings")
django.setup()

# 主页视图
def index(request):
    return render(request,'index.html')


# 板块视图
def section(request, section_name: str):
    return HttpResponse("这是板块视图,你正在查看 " + section_name + " 板块")


# 请求帖子列表,JS的api，用户不会直接访问
def get_topic(request):
    response = {'info': 'Your request information as below',
                'start': request.GET['start'],
                'num': request.GET['num']
                }
    return HttpResponse(json.dumps(response), content_type='application/json')


# 帖子视图
def topic(request, topic_id: int):
    return HttpResponse("这是贴子视图," + "你正在查看帖子ID " + str(topic_id))

class CustomBackend(ModelBackend):
    def authenticate(self,request,username=None,password=None):
        try:
            user=User.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

def userlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        authentication=CustomBackend()
        user=authentication.authenticate(request,email,password)
        if user is not None:
            login(request,user)
            print('USER LOGIN:',user)
            return redirect(reverse('bbs:index'))
        else:
            errmsg=u'用户名或密码出错'
            return render(request,'login.html',{'errmsg':errmsg})
    return render(request,'login.html')


def usersignup(request):
    if request.method == 'POST':
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        password_confirm = request.POST.get("password_confirm", "")
        email = request.POST.get("email", "")

        form = UserForm(request.POST)
        errors = []
        #验证表单是否正确
        if form.is_valid():
            current_site = get_current_site(request)
            site_name = current_site.name
            domain = current_site.domain
            title = u"欢迎来到 %s ！" % site_name
            message = u"你好！ %s ,感谢注册 %s ！\n\n" % (username,site_name) + \
                      u"请牢记以下信息：\n" + \
                      u"用户名：%s" % username+"\n" + \
                      u"邮箱：%s" % email+"\n" + \
                      u"网站：http://%s" % domain+"\n\n"
            try:
                send_mail(title, message, EMAIL_FROM, [email])
            except Exception as e:
                logger.error(
                    u'[UserControl]用户注册邮件发送失败:[%s]/[%s]' % (username, email))
                return HttpResponse(u"发送邮件错误!\n注册失败", status=500)

            User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            print("USER CREATED:",user)
            return render(request,'login.html')
        else:
            #如果表单不正确,保存错误到errors列表中
            for k, v in form.errors.items():
                #v.as_text() 详见django.forms.util.ErrorList 中
                errors.append(v.as_text())
            return render(request,'signup.html',{"errors":errors})

    else:
        #next = request.GET.get('next',None)
        #if next is None:
        #next = reverse_lazy('index')
        return render(request,'signup.html')





def userlogout(request):
    logout(request)
    return redirect(reverse('bbs:index'))
