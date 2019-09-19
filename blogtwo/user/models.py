from django.db import models
from db.base_model import BaseModel
from django.contrib.auth.models import AbstractUser


class User(AbstractUser, BaseModel):
    '''用户模型类'''
    nid = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=11, null=True, unique=True)
    avatar = models.FileField(upload_to="avatars/", default="avatars/default.png", verbose_name="头像")
    email = models.CharField(max_length=30, null=True,unique=True)
    focus_num = models.SmallIntegerField(default=0)   # 关注数量
    bfocus_num = models.SmallIntegerField(default=0)   # 被关注数量
    is_super = models.CharField(max_length=20, default=False)    # 是否是超级用户
    is_active = models.CharField(max_length=32,default=False)  # 是否激活

    blog = models.OneToOneField(to="Blog", to_field='nid', null=True)

    def __str__(self):
        return self.username

    class Meta:
        # abstract=True
        db_table = 'df_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Blog(BaseModel):
    """
    博客信息
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)  # 个人博客标题
    site = models.CharField(max_length=32, unique=True)  # 个人博客后缀
    theme = models.CharField(max_length=32)  # 博客主题

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'df_blog'
        verbose_name = "blog站点"
        verbose_name_plural = verbose_name

