from django.shortcuts import render,redirect
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from django.urls import reverse
# Create your views here.
class RegisterView(View):
    def get(self,request):
        return render(request,"register.html")#static文件尚未编写，此处渲染页面为注册页面
    def post(self,request):
        username=request.POST.get("username")
        password=request.POST.get("password")
        hash_password=make_password(password)#对密码加密入库
        User.objects.create(
            username=username,
            password=hash_password
        )
        return rediect(reverse("index"))
        return  HttpResponse("注册成功")
    写前端页面的时候一定要记得加{% crsf_token %}防跨站攻击
class LoginView(View):
    def get(self,request):
        return render(request,"login.html")#static文件尚未编写，此处渲染页面为注册页面
    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('username')
        try:
            user=User.objects.get(username=username)
        except User.DoesNotExist:
            return render(request,"login.html")
        if not check_password(password,user.password):
            return render(request,"login.html")
        request.session['id']=user.id
        request.session['name']=user.username
        return redirect(reverse('index'))
