from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# 1.定义视图函数index，必须要返回一个 HttpRequest 对象
# 2.然后去进行url配置，建立url地址和视图的对应关系
# 想让用户输入 http://127.0.0.1:8000/总路由+子路由 时可以显示下面的内容
def index(request):
    "进行处理，和M和T进行交互"
    #
    """
        之前是直接返回的内容:
    text = "<div style='color:hotpink; width:300px; height:300px; background: orange'>Hello world</div>"
    return HttpResponse(text)
    """
    # 现在是要读取模板中的内容来返回
    """
    这是视频1.8版本的原理讲解，在3.2版本这会报错的，所以还是直接使用系统提供的render()渲染吧
    导包 from django.template import loader, RequestContext
    # 1.加载模板文件，
    temp = loader.get_template("booktest/index.html")  # 注意路径
    # 2.定义模板上下文，给模板传递数据，没有的话可以传一个 空字典
    context = RequestContext(request, {})   # 要用RequestContext这个类对象
    # 3.模板渲染
    res_html = temp.render(context)
    return HttpResponse(res_html)
    """
    replace_data = dict(
        my_content="这是替换的第一个参数",
        my_list=list(range(10))
    )
    # 不用替换数据就不用传第三个参数,可以为空
    return render(request, "booktest/index.html", replace_data)

# 注意导包不能写 from models import BookInfo   运行会出出错的
from booktest.models import BookInfo
def show_book(request):
    bs = BookInfo.objects.all()  # 获取所有书的对象
    replace_data = dict(
        book_objs=bs
    )
    return render(request, "booktest/books.html", replace_data)


from booktest.models import HeroInfo
def hero_info(request, book_id):
    # 这是获取 HeroInfo 表中的所有英雄
    # hs = HeroInfo.objects.all()

    # get只能获取单条数据，如果是多条数据，就会报错，如果只有一条，这不会报错，html模板里的循环就会报错
    # HeroInfo.objects.get(id=book_id)


    # 获取指定id的书这个对象
    book_obj = BookInfo.objects.get(id=book_id)      # 一条数据，不用循环的话，就用get

    # 获取指定书中的英雄,为空不会报错，也不会进到模板的循环中去
    # hs = HeroInfo.objects.filter(hbook_id=book_id)  # 注意这个字段名
    # 除了filter这种写法，还有：本就获取到了 book_obj 这本书的对象，那就
    hs = book_obj.heroinfo_set.all()


    replace_data = dict(
        hero_objs=hs,
        book_obj=book_obj
    )
    return render(request, "booktest/heros.html", replace_data)   # 注意路径前往别写成了booktest.heros.html
