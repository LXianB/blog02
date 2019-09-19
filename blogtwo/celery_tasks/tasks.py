# !/user/bin/env python
# -*- coding:utf-8 -*-
from django.conf import settings
from django.core.mail import send_mail
import time
# 使用celery
from celery import Celery

# 在任务处理者一端加这几句（django黄金初始化)
# import os
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogtwo.settings")
# django.setup()


# broker系统里面启动redis 执行 ps aux | grep redis
app = Celery('celery_tasks.tasks',broker='redis://127.0.0.1:6379/8')  # 使用功能redis作为中间人 8代表使用8号数据库


# 定义任务函数
@app.task
def send_register_active_email(user,token):
    """发送激活邮件"""
    # 发邮件
    subject = '博客欢迎信息'
    message = ''
    send = settings.EMAIL_FROM
    recipient = [user.email]  # 收件人邮箱，一次可以发送给多个邮箱
    html_message = "<h2>%s,欢迎注册本博客，恭喜您成为本博客用户</h2>请点击以下链接激活账号<a href='http://127.0.0.1:8000/user/active/%s'>http://127.0.0.1:8000/user/active/%s</a>" % (
    user.username, token, token)
    # send_mail阻塞执行，等到邮件发送了，页面才能跳转到index，可以使用celery异步执行，
    send_mail(subject, message, send, recipient_list=recipient, html_message=html_message)
    time.sleep(1)