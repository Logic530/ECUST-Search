#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


# 板块数据模型
class Section(models.Model):
    # 板块标题，字符串，最大10
    title = models.CharField(max_length=10, unique=True, verbose_name="板块标题")
    # 板块描述
    description = models.CharField(max_length=300, verbose_name="板块描述")
    # 板块管理员，多对多关系，不知道配置是否正确
    admin = models.ManyToManyField(User, verbose_name="板块管理员")

    class Meta:
        verbose_name = "板块"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 标签数据类型
class Tag(models.Model):
    # 标签名称
    name = models.CharField(max_length=10, unique=True, verbose_name="标签名称")

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 帖子数据模型
class Topic(models.Model):
    # 贴子标题，字符串，最大长度30
    title = models.CharField(max_length=30, verbose_name="标题")
    # 帖子内容，字符串，最大长度300
    content = models.TextField(max_length=300, verbose_name="内容")
    # 发帖人ID,应该是外键，但是我不懂数据库，先不做
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="发帖用户")
    # 发帖时间
    datetime = models.DateTimeField(auto_now=True, verbose_name="发帖时间")
    # 帖子所属板块，应该是外键
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name="所属板块")

    # 帖子所属板块标题
    @property
    def section_title(self):
        return self.section.title

    # 点赞用户列表
    liked_users = models.ManyToManyField(User, related_name="liked_user", blank=True, verbose_name="点赞用户列表")
    # 帖子被浏览数
    viewed_count = models.IntegerField(default=0, verbose_name="帖子被浏览次数")
    # 是否被解决
    solved = models.BooleanField(default=False, verbose_name="是否被解决")
    # 标签
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="标签")

    # 回复计数
    @property
    def reply_count(self):
        if self.comment_set:
            return self.comment_set.count()
        else:
            return 0

    """    
    # 最近回复时间
    @property
    def latest_reply_time(self):
        if self.comment_set:
            return self.comment_set[0].datetime
        else:
            return None
    """

    # 点赞计数
    @property
    def liked_count(self):
        return self.liked_users.count()

    class Meta:
        verbose_name = "帖子"
        verbose_name_plural = verbose_name
        ordering = ['-datetime']

    def __str__(self):
        return self.title


# 评论数据模型
class Comment(models.Model):
    # 评论内容
    content = models.TextField(max_length=300, verbose_name="评论内容")
    # 评论发送者ID，外键，不知配置是否正确
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="评论发送用户")
    # 评论发送日期
    datetime = models.DateTimeField(auto_now=True, verbose_name="评论发送日期")
    # 评论所属帖子,外键，不知配置是否正确
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name="评论所属帖子")
    # 评论被点赞数
    liked_count = models.IntegerField(default=0, verbose_name="评论被点赞次数")

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.owner.username + " 在 " + str(self.datetime) + " 发布于 " + self.topic.title + " 的评论"


# 用户档案模型，用于扩展用户信息字段，这里仅存放论坛APP相关的信息字段
class Profile(models.Model):
    # 指定一对一用户关系
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="档案对应用户")
    friends=models.ManyToManyField('self',blank=True,related_name='friends')
    phone=models.PositiveIntegerField(verbose_name='电话号码')

    # 没想好有什么，可以弄个徽章什么的？
    # 或者是论坛的积分
    # points = models.IntegerField()

    def __str__(self):
        return self.user.username + "的档案"
