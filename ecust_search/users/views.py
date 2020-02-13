from django.shortcuts import render,redirect

from django.contrib.auth.hashers import make_password,check_password
from django.urls import reverse
from users.models import User

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from forum.form import MessageForm, PostForm, LoginUserForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.models import get_current_site
from django.core.mail import send_mail


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
def userlogin(request, template_name='login.html'):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next = request.POST['next']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            user.levels += 1  #登录一次积分加 1
            user.save()
        return HttpResponseRedirect(next)
    else:
        next = request.GET.get('next', None)
        if next is None:
            next = reverse_lazy('index')
        return render_to_response(template_name, {'next': next})


#用户注销
def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('index'))


#用户注册
def userregister(request):
    if request.method == 'POST':
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        password_confirm = request.POST.get("password_confirm", "")
        email = request.POST.get("email", "")

        form = LoginUserForm(request.POST)
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
            from_email = None
            try:
                send_mail(title, message, from_email, [email])
            except Exception as e:
                logger.error(
                    u'[UserControl]用户注册邮件发送失败:[%s]/[%s]' % (username, email))
                return HttpResponse(u"发送邮件错误!\n注册失败", status=500)

            new_user = form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
        else:
            #如果表单不正确,保存错误到errors列表中
            for k, v in form.errors.items():
                #v.as_text() 详见django.forms.util.ErrorList 中
                errors.append(v.as_text())

        return render_to_response('user_ok.html', {"errors": errors})

    else:
        #next = request.GET.get('next',None)
        #if next is None:
        #next = reverse_lazy('index')
        return render_to_response('register.html')


