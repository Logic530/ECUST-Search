from django.db import models
class Category(models.Model):
    name=models.CharField(max_length=20,unique=True,verbose_name="分类名称")
    parent=models.ForeignKey("self",on_delete=models.SET_NULL,null=True,blank=True,verbose_name="上一级ID")
    def __str__(self):
        return self.name
    class Meta:
        db_table="home_category"
        verbose_name="分类管理"
        verbose_name_plural=verbose_name
