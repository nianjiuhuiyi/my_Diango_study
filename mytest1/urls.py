"""mytest1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from booktest import views
urlpatterns = [
    # 注意path这里面不能正则了
    path('admin/', admin.site.urls),
    # 这行是我加的 （前面都没有 / ）
    path(r"index/", include("booktest.urls")),
    path("", include("booktest.urls")),  # 登录页面


    # 下面这两行跟path(r"index", include("booktest.urls"))是一个效果，
    # 说明path可以跟地址，也可以跟一个映射函数
    #from booktest import views
    # path(r"index123/", views.index)
]


"""
 这是1.8这版本，即1.x的版本的写法，在后面是错的
 老版本还可以正则，新版本不行了(暂时不知道怎么破)
 
from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url("admin/", include(admin.site.urls)),
    url(r"^index/", include("booktest.urls"))
]

"""

