# !/user/bin/env python
# -*- coding:utf-8 -*-

# 文件名字固定
# 定义模型类
from haystack import indexes
# 导入你的模型类
from .models import Article

# 指定对于某个类的某些数据建立索引
# 索引类名一般是:模型类名+Index

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    # 索引字段，use_template=True指定根据表中的哪些字段建立索引，把说明放在一个文件中
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        # 返回你的模型类
        return Article

    # 建立索引的数据
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
