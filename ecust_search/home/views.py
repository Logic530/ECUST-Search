from django.shortcuts import render
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
# Create your views here.
class IndexView(View):
    def get(self,request):
        return HttpResponse(request,"Index.html")#static文件尚未编写，此处渲染页面为注册页面