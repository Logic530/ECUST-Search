from django.http import HttpResponse, JsonResponse
from .serializers import TopicSerializer
from .models import Topic


# 主页视图
def index(request):
    return HttpResponse("这是BBS主页视图")


# 板块视图
def section(request, section_name: str):
    return HttpResponse("这是板块视图,你正在查看 " + section_name + " 板块")


# 帖子视图
def topic(request, topic_id: int):
    return HttpResponse("这是贴子视图," + "你正在查看帖子ID " + str(topic_id))


def get_recent_topic(request):
    if request.method == 'GET':
        topics = Topic.objects.all().order_by('-datetime')
        serializer = TopicSerializer(topics, many=True)
        return JsonResponse(serializer.data, safe=False)


'''
def get_hot_topic(request):
    if request.method == 'GET':
        # 下面这句没法用，不知道怎样才能按回复数排序
        topics = Topic.objects.all().order_by('reply_count')
        serializer = TopicSerializer(topics, many=True)
        return JsonResponse(serializer.data)
'''
