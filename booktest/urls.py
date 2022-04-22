from django.urls import path, re_path
from booktest import views

urlpatterns = [
    path('123/', views.index),
    path('book/', views.show_book),
    re_path("book/(\d+)", views.hero_info)   # (\d+) 正则表达式的组的值才会被传给函数当另外的参数
]