from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=20,unique=True,verbose_name="用户名")
    password=models.CharField(max_length=100,verbose_name="密码")
    def __str__(self):
        return self.username
    class Meta:
        db_table="bbs_user"
        verbose_name='用户管理'
        verbose_name_plural=verbose_name
class LoginUser(AbstractUser):
    levels = models.PositiveIntegerField(default=0, verbose_name=u'积分')
    avatar = models.CharField(
        max_length=200, default='/static/tx/default.jpg', verbose_name=u'头像')
    privilege = models.CharField(max_length=200, default=0, verbose_name=u'权限')
    friends = models.ManyToManyField(
        'self', blank=True, null=True, related_name='friends')

    class Meta:
        db_table = 'loginuser'
        verbose_name_plural = u'用户'
        ordering = ['-date_joined']

    def __unicode__(self):
        return self.get_username()

    def checkfriend(self, username):
        if username in self.friends.all():
            return True
        else:
            return False