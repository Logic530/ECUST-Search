from django.shortcuts import render
from django.http import HttpResponse


# 主页视图
def index(request):
    return HttpResponse("这是BBS主页视图")


# 板块视图
def section(request, section:str):
    return HttpResponse("这是板块视图,你正在查看 " + section + " 板块")


# 帖子视图
def topic(request, topic_id:int):
    return HttpResponse("这是贴子视图," + "你正在查看帖子ID " + str(topic_id))
