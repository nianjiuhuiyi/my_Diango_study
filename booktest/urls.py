from django.urls import path, re_path
from booktest import views

urlpatterns = [
    path('123/', views.index),
    path('book123/', views.show_book),
    re_path("book/(\d+)/", views.hero_info),   # (\d+) 正则表达式的组的值才会被传给函数当另外的参数
    path("book/create/", views.create),   # 添加一本固定的书
    re_path("book/delete/(\d+)/", views.delete),  # 添加书的删除按钮

    path("login/", views.login),  # 登录页面
    path("login_check/", views.login_check),  # 登录检查

    path("set_cookie", views.set_cookie),
    path("get_cookie", views.get_cookie),  # cookie

    path("set_session", views.set_session),
    path("get_session", views.get_session),  # session

    path("inherit", views.inherit),  # 模板继承

    path("trans", views.trans),  # 转义

    path("verifyCode", views.verifyCode),  # 显示验证码

    path("url_reverse", views.url_reverse),  # url反向解析

    path("ours", views.ours),

    path("upload", views.upload),  # 上传图片的展示页面
    path("pic_handle", views.pic_handle),  # 上传的图片的后台处理
]
