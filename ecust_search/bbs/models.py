from django.db import models
from django.contrib.auth.models import User


# 板块数据模型
class Section(models.Model):
    # 板块标题，字符串，最大10
    title = models.CharField(max_length=10)
    # 板块描述
    description = models.CharField(max_length=300)
    # 板块管理员，多对多关系，不知道配置是否正确
    admin = models.ManyToManyField(User)


# 帖子数据模型
class Topic(models.Model):
    # 贴子标题，字符串，最大长度30
    title = models.CharField(max_length=30)
    # 帖子内容，字符串，最大长度300
    content = models.CharField(max_length=300)
    # 发帖人ID,应该是外键，但是我不懂数据库，先不做
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # 发帖时间
    datetime = models.DateTimeField()
    # 帖子所属板块，应该是外键
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    # 帖子被点赞次数
    liked_count = models.IntegerField()


# 评论数据模型
class Comment(models.Model):
    # 评论内容
    content = models.CharField(max_length=300)
    # 评论发送者ID，外键，不知配置是否正确
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # 评论发送日期
    datetime = models.DateTimeField()
    # 评论所属帖子,外键，不知配置是否正确
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # 评论被点赞数
    liked_count = models.IntegerField()
