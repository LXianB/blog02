from django.db import models
from db.base_model import BaseModel
from user.models import User

# Create your models here.


class Article(BaseModel):
    """文章"""
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name="文章标题")  # 文章标题
    desc = models.CharField(max_length=255)  # 文章描述
    # 评论数
    comment_count = models.IntegerField(verbose_name="评论数", default=0)
    # 点赞数
    up_count = models.IntegerField(verbose_name="点赞数", default=0)
    # 踩
    down_count = models.IntegerField(verbose_name="踩数", default=0)
    # 转发数
    repeat_count = models.IntegerField(verbose_name="转发数",default=0)

    user = models.ForeignKey("user.User", to_field="nid")
    sorts = models.ManyToManyField(  # 中介模型
        to="Sort",
        through="ArticleToSort",
        through_fields=("article", "sort"),  # 注意顺序！！！
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'df_article'
        verbose_name = "文章"
        verbose_name_plural = verbose_name


class ArticleDetail(BaseModel):
    """文章详情表"""
    nid = models.AutoField(primary_key=True)
    content = models.TextField()
    article = models.OneToOneField(to="article.Article", to_field="nid")

    class Meta:
        db_table = 'df_articledetail'
        verbose_name = "文章详情"
        verbose_name_plural = verbose_name


class Sort(BaseModel):
    '''文章分类表'''
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'df_sort'
        verbose_name = '分类表'
        verbose_name_plural = verbose_name


class ArticleToSort(BaseModel):
    """
    文章和分类的多对多关系表
    """
    nid = models.AutoField(primary_key=True)
    article = models.ForeignKey(to="article.Article", to_field="nid")
    sort = models.ForeignKey(to="article.Sort", to_field="nid")

    def __str__(self):
        return "{}-{}".format(self.article.title, self.sort.title)

    class Meta:
        db_table = 'df_artoso'
        unique_together = (("article", "sort"),)
        verbose_name = "文章-标签"
        verbose_name_plural = verbose_name


class ArticleUpDown(BaseModel):
    """点赞表"""
    nid = models.AutoField(primary_key=True)
    user = models.ForeignKey(to="user.User", null=True)   # 点踩的用户id
    article = models.ForeignKey(to="article.Article", null=True)   # 文章id
    is_up = models.BooleanField(default=True)     # 赞踩

    class Meta:
        db_table = 'df_updown'
        unique_together = (("article", "user"),)
        verbose_name = "文章点赞"
        verbose_name_plural = verbose_name


class Comment(BaseModel):
    """评论表"""
    nid = models.AutoField(primary_key=True)
    article = models.ForeignKey(to="article.Article", to_field="nid")
    user = models.ForeignKey(to="user.User", to_field="nid")
    content = models.CharField(max_length=255)  # 评论内容
    # create_time = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey("self", null=True, blank=True)  # blank=True 在django admin里面可以不填

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'df_comment'
        verbose_name = "评论"
        verbose_name_plural = verbose_name


class Forward(BaseModel):
    """转发表"""
    nid = models.AutoField(primary_key=True)
    article = models.ForeignKey(to="article.Article", null=True)    # 被转发的文章id
    user = models.ForeignKey(to="user.User", null=True)    # 转发的用户id

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'df_forward'
        unique_together = (("article", "user"),)
        verbose_name = "文章转发"
        verbose_name_plural = verbose_name


# class Careful(BaseModel):
#     """关注表"""
#     nid = models.AutoField(primary_key=True)
#     active_user = models.ForeignKey(to="user.User", null=True)     # 主动关注的用户
#     passive_user = models.ForeignKey(to="user.User", null=True)
#
#     def __str__(self):
#         return self.active_user
#
#     class Meta:
#         db_table = 'df_focus'
#         unique_together = (("user", "bu"),)
#         verbose_name = "关注"
#         verbose_name_plural = verbose_name


class LeavMess(BaseModel):
    """留言表,此处注意related_name的用法,同一个表中多个外键关联其他表"""
    nid = models.AutoField(primary_key=True)
    acti = models.ForeignKey(to="user.User",related_name="UserInfo_con")    # 主动留言的用户的id
    psive = models.ForeignKey(to="user.User")     # 被留言用户的ID
    contentq = models.TextField(max_length=600)              # 留言的内容

    def __str_(self):
        return self.acti

    class Meta:
        db_table = 'df_leavemess'
        verbose_name = "留言"
        verbose_name_plural = verbose_name

