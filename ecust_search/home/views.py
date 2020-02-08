from django.shortcuts import render
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from home.models import Category
# Create your views here.
class IndexView(View):
    def get(self,request):
        is_login=request.session.get('id')
        name=request.session.get('name')
        categories=Category.objects.all()
        context={
            "is_login":is_login,
            "name":name,
            "categories":categories
        }
        return render(request,"index.html",context=context)#static文件尚未编写，此处渲染页面为注册页面