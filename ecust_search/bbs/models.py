from django.db import models
from django.contirb.auth.models import AbstractUser


# 帖子数据模型
class Topic(models.Model):
    # 贴子标题，字符串，最大长度30
    topic_title = models.CharField(max_length=30)
    # 帖子内容，字符串，最大长度300
    topic_description = models.CharField(max_length=300)
    # 发帖人ID,应该是外键，但是我不懂数据库，先不做

    # 发帖时间
    topic_publish_datetime = models.DateTimeField()
    # 帖子所属板块，应该是外键

    # 帖子被点赞次数
    topic_liked_count = models.IntegerField()


# 评论数据模型
class Comment(models.Model):
    # 评论内容
    comment_content = models.CharField(max_length=300)
    # 评论发送者ID，外键

    # 评论发送日期
    comment_datetime = models.DateTimeField()
    # 评论所属帖子,外键

    # 评论被点赞数
    comment_liked_count = models.IntegerField()
    # 评论被踩数
    comment_disliked_count = models.IntegerField()
    # 帖子ID,外键


# 板块数据模型
class Section(models.Model):
    # 板块名称，字符串，最大10
    section_name = models.CharField(max_length=10)
    # 还有一些别的什么？我不知道了


class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True, verbose_name='电话号码')
    privilege = models.CharField(max_length=200, default=0, verbose_name="权限")
    friends = models.ManyToManyField('self', blank=True, null=True, related_name='friends')

    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-date_joined']

    def __str__(self):
        return self.username

    def checkfriend(self, username):
        if username in self.friends.all():
            return True
        else:
            return False
