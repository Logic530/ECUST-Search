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