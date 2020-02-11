from django.shortcuts import render,redirect
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from django.urls import reverse
from users.models import User
# Create your views here.
class RegisterView(View):
    def get(self,request):
        return render(request,"register.html")#static文件尚未编写，此处渲染页面为注册页面
    def post(self,request):
        username=request.POST.get("username")
        password=request.POST.get("password1")
        password_confirm=request.POST.get("password2")
        hash_password=make_password(password)#对密码加密入库
        if password == password_confirm:
            User.objects.create(
                username=username,
                password=hash_password
            )
            return redirect(reverse('home:index'))
        else:
            return redirect(reverse("user:register"))
class LoginView(View):
    def get(self,request):
        return render(request,"login.html")#static文件尚未编写，此处渲染页面为注册页面
    def post(self,request):
        username=request.POST.get("username")
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except User.DoesNotExist:
            return render(request,'login.html')
        if not check_password(password,user.password):
            error_msg = "用户名或密码错误"
            return render(request, 'login.html', {'error_msg': error_msg})
        request.session['id'] = user.id
        request.session['name'] = user.username
        return redirect(reverse('home:index'))
