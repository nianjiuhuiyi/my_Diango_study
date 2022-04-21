from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# 1.定义视图函数index，必须要返回一个 HttpRequest 对象
# 2.然后去进行url配置，建立url地址和视图的对应关系
# 想让用户输入 http://127.0.0.1:8000/总路由+子路由 时可以显示下面的内容
def index(request):
    "进行处理，和M和T进行交互"
    text = "<div style='color:hotpink; width:300px; height:300px; background: orange'>Hello world</div>"
    return HttpResponse(text)
