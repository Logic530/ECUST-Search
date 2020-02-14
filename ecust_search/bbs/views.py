from django.http import HttpResponse
import json


# 主页视图
def index(request):
    return HttpResponse("这是BBS主页视图")


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
