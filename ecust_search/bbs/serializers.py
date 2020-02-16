from .models import Topic, Comment
from rest_framework import serializers


# 帖子的Json转化器类型
class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = ['title', 'content', 'liked_count', 'viewed_count', 'reply_count', 'solved', 'datetime',
                  'section_title']
