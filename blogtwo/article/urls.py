"""blogtwo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from article import views
from django.conf import settings
from django.views.static import serve
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', views.kong, name='kong'),    # 当网址什么都不填时重定向到index
    url(r'^index/', views.Index.as_view(), name='index'),  # 首页
    url(r'^search/', include('haystack.urls')),   # 全文检索框架
    url(r'^add/', views.ArticleAdd.as_view(), name='article_add'),    # 博客添加
    url(r'^detail/(?P<username>.*)/(?P<pk>.*)/', views.ArticleDetail.as_view(), name='detail'),     # 博客详情页
    # media相关的路由设置
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    url(r'^upload/', views.upload, name='upload'),

]
