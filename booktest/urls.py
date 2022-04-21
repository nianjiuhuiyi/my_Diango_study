from django.urls import path
from booktest import views

urlpatterns = [
    # 前面总路由有了 index ,子路由是123，那访问就应该是 :port/index/123
    path('123/', views.index),
]