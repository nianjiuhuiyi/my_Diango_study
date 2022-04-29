from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# 1.定义视图函数index，必须要返回一个 HttpRequest 对象
# 2.然后去进行url配置，建立url地址和视图的对应关系
# 想让用户输入 http://127.0.0.1:8000/总路由+子路由 时可以显示下面的内容
# /index/123
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
# /book
def show_book(request):
    bs = BookInfo.objects.all()  # 获取所有书的对象
    replace_data = dict(
        book_objs=bs
    )
    return render(request, "booktest/books.html", replace_data)


from booktest.models import HeroInfo
# /book/(\d+)
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


import datetime
from django.http import HttpResponseRedirect
# /book/create
def create(request):
    # 创建一本书，为了简单，信息都是固定的
    b = BookInfo()  # 新建一个对象
    b.btitle = "这是新建的一本固定的书"
    b.bpub_date = datetime.date(1997, 6, 27)
    b.save()  # 把创建的数据报存

    # 上面操作完了，还是重定向(就是再次访问)回这个原来的页面（一定要的）用于展示
    return HttpResponseRedirect("/index/book")

from django.shortcuts import redirect
# /book/delete/(\d+)
def delete(request, book_id):
    b = BookInfo.objects.get(id=book_id)    # 是objects，别写错了
    b.delete()    # 删除

    # return HttpResponseRedirect("/index/book")
    return redirect("/index/book")  # 跟上面效果一模一样，推荐这个吧


# /login
def login(request):
    """显示登录页面"""
    if request.session.has_key("isLogin"):
        # 有值就代表login_check()函数中登陆成功，并设置了 request.session[""isLogin]
        return redirect("/index/123/")

    # 下面login_check在登录成功时保存了用户名的cookie，这里去取来判断，有就直接先填上
    # userName = request.POST.get("userName")  # 注意前面别写错了，用的是cookie
    userName = request.COOKIES.get("userName")  # 当做字典来用的
    replace_data = dict()
    if userName is not None:
        replace_data["userName"] = userName
    return render(request, "booktest/login.html", replace_data)


# /login_check
def login_check(request):
    """
    request传过来的对象的数据都在这个里面
    """
    print(type(request.POST))   # 类型是<class 'django.http.request.QueryDict'>
    print(request.method)  # 获取请求方式，一般为 POST 或 GET
    # 我们表单设计的是POST方式，浏览器直接敲这个地址 /login_check 访问的方式是GET

    # 1.获取提交的用户名和密码 (html中的input标签中的name值是什么，这里的key就是什么)
    userName = request.POST.get("userName")
    password = request.POST.get("password")

    # 2.数据库查询用户名、密码进行校验，这里就是模拟一下
    if userName == "admin" and password == "123":
        # # 成功，那就跳转到一个页面 (这是前面简单的代码)
        # return redirect("/index/123/")

        # 以下是只记住登录成功的用户名
        response = redirect("/index/123/")  # 这个对象本质也是HttpResponse的
        # 如果勾选了复选框，返回的就是字符串“on”，没勾选返回的就是一个None
        remember = request.POST.get("my_remember")
        if remember is not None:
            response.set_cookie("userName", userName)  # 关闭浏览器即过期，方便调试
            # response.set_cookie("userName", userName, max_age=14*24*3600)

        # 在登录成功后，直接session记住登录状态，通过添加session键值对
        request.session["isLogin"] = True

        return response
    else:
        return HttpResponse("错误！")


"""开始cookie的学习"""

# /set_cookie
def set_cookie(request):
    """设置cookie信息"""
    response = HttpResponse("设置cookie")
    # 设置一个cookie信息，名字为num，值为1，，
    # .set_cookie是HttpResponse对象带有的方法
    # response.set_cookie("num", 123)
    # response.set_cookie("num_new", 456)  # 可设置多个cookie
    # 设置过期时间，两种方式(别不设置14天过期)
    # 方式一：
    response.set_cookie("num", 123, max_age=14*24*3600)  # max_age是到期时间剩余秒数
    # 方式二：
    from datetime import datetime, timedelta
    response.set_cookie("num_new", 456789, expires=datetime.now() + timedelta(days=14))

    return response  # 返回给浏览器


# /get_cookie
def get_cookie(request):
    """浏览器发过来后，获取cookie信息"""
    num = request.COOKIES["num"]
    # 获取到前面自己设的cookie值，然后返回给页面
    return HttpResponse(num)



"""开始session的学习"""
# /set_session
def set_session(request):
    # 一样session也可以存很多键值对
    request.session["userName"] = "admin"
    request.session["age"] = 18
    # session中，int就是int，而cookie中键、值都是str
    return HttpResponse("session设置成功")


# /get_session
def get_session(request):
    """仅仅是模拟从服务器拿到session的数据，然后显示出来"""
    userName = request.session.get("userName")
    age = request.session.get("age")  # 这个节结果是int哦
    # 理论应该判等一下是否为None的
    return HttpResponse("获取session结果：" + userName + " : " + str(age))


# /inherit
def inherit(request):
    return render(request, "booktest/son1.html")


# /trans
def trans(request):
    """转义"""
    data = {"my_content": "<h1>这是一句话</h1>"}
    return render(request, "booktest/trans_mean.html", data)


# /verifyCode
def verifyCode(request):
    """生成一个随机码用于展示"""
    import numpy as np
    from PIL import Image, ImageDraw, ImageFont
    from django.utils.six import BytesIO

    # font = ImageFont.truetype("arial.ttf", 35)
    font = ImageFont.truetype("bahnschrift.ttf", 40)  # 这个只要用系统中有的字体，就不会报错

    # ubuntu的字体路径为 /usr/share/fonts/truetype/freeFont  一个常用字体 FreeMono.ttf

    image = Image.new("RGB", (240, 60))
    image = np.array(image)
    image_data = np.random.randint(65, 255, (60, 240, 3))
    image[...] = image_data[...]

    image = Image.fromarray(image)
    draw = ImageDraw.Draw(image)
    for i in range(4):
        font_color = np.random.randint(0, 255, (1, 3)).tolist()[0]
        draw.text((i * 60 + 10, 10), text=chr(np.random.randint(65, 90 + 1)), fill=tuple(font_color), font=font)

    # 可以搞个session的键值对把生成的资格随机字符存进去，用于后续验证
    # request.session["verifyCode"] = "四个生成的字符"

    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    image.save(buf, "png")
    return HttpResponse(buf.getvalue(), "image/png")  # 这后面的 "image/png" 应该是固定写法


# /url_reverse
def url_reverse(request):
    """指定的html模板里面是登录页面的超链接；学习失败了"""
    return render(request, "booktest/url_reverse.html")


# 通过装饰器来禁止部分ip访问
# BLOCK_IPS = ["192.168.108.218"]
# def block_ip(view_func):
#     def wrapper(request, *args, **kwargs):
#         user_ip = request.META["REMOTE_ADDR"]
#         if user_ip in BLOCK_IPS:
#             return HttpResponse("403 Forbidden")
#         else:
#             return view_func(request, *args, **kwargs)
#     return wrapper
# @block_ip
# def ours(request):
#     pass


# /ours
def ours(request):
    # 这是一个可以看到django所有设置
    from django.conf import settings
    # print(settings.STATICFILES_DIRS)  # 查看查找静态文件配置的地址

    user_ip = request.META["REMOTE_ADDR"]  # 获取访问者的ip地址
    print("这是视图函数里面被执行的打印：", user_ip)
    # a = '1' + 1  # 让服务器出错，加这么一行就好了
    return render(request, "booktest/ours.html")


# /upload
def upload(request):
    """图片上传页面"""
    return render(request, "booktest/upload.html")


# /pic_handle
from booktest.models import PicTest
from django.conf import settings
def pic_handle(request):
    """表单点击上传的图片的处理（放后台处理，就没有对应的页面展示）"""
    # 1、获取上传文件的处理对象
    image = request.FILES["my_pic"]  # “my_pic”是file的input标签的name
    # print(type(image))
    # from django.core.files import uploadedfile
    # <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
    # <class 'django.core.files.uploadedfile.TemporaryUploadedFile'>

    image_name = image.name    # 有一个name属性,获取到上传文件的名字
    # print(image_name)
    # print(image.size)  # 以字节为单位
    # print(image.content_type)
    # # 还有一个属性 image.chunks()  # 它的返回值是一个生成器，每次返回这个文件一块的内容

    # 2、将二进制形式的文件保存起来
    abs_save_path = "{}/booktest/{}".format(settings.MEDIA_ROOT, image_name)
    with open(abs_save_path, "wb") as fp:
        for content in image.chunks():
            fp.write(content)

    # 3、在数据库中保存上传记录
    PicTest.objects.create(goods_pic=f"booktest/{image_name}")   # goods_pic是PicTest这个类的一个属性

    # from django.conf.global_settings import FILE_UPLOAD_HANDLERS
    # print(FILE_UPLOAD_HANDLERS)

    return HttpResponse("ok")


from booktest.models import AreaInfo
from django.core.paginator import Paginator
# /all_area
def all_area(request):
    """ 展示地区表中的所有数据 """
    # 1、查询出所有的地区信息
    datas = AreaInfo.objects.all()
    # 2、分页，每页显示10条
    my_paginator = Paginator(datas, 10)  # 总的内容都在my_paginator这里面，只是被分页了

    # print(my_paginator.num_pages)  # 获取总页数 如 341
    # print(my_paginator.page_range)  # 获取总页码的列表 如 range(1, 342)

    # 3、获取第一页的内容 （这就是分页取内容）
    page = my_paginator.page(3)  # page是Page类的实例对象
    # print(page.number)
    # page.object_list  # 拿到的是这一页数据的查询集
    # page.paginator   就是又拿到了实例对象 my_paginator
    # print(page.has_previous())   # 返回布尔值，判断当前页是否有前一页
    # print(page.has_next())       # 返回布尔值，判断当前页是否有下一页
    # print(page.previous_page_number())  # 返回前一页的页码，如果是在第1页，这会报错
    # print(page.next_page_number())  # 返回下一页的页码，如果是在最后一页，这会报错

    return render(request, "booktest/all_area.html", {"areas": datas})  # 这是所有的数据  （这两行注释其中一个看效果）
    # return render(request, "booktest/all_area.html", {"areas": page.object_list})  # 第一页的数据


# /page_area  或者 /page_area13  这就是/page_area页码
def page_area(request, page_num):
    """分页展示数据"""
    # 1、查询出所有的地区信息
    # datas = AreaInfo.objects.all()
    datas = AreaInfo.objects.filter(level=1)
    # 2、分页，每页显示10条 (没说是第几页，page_num就是一个空字符串，就默认来到第1页)
    if not page_num:
        page_num = 1
    my_paginator = Paginator(datas, 10)  # 总的内容都在my_paginator这里面，只是被分页了

    page = my_paginator.page(page_num)
    replace_data = dict(
        # my_paginator=list(my_paginator.page_range),
        my_page_range=my_paginator.page_range,
        my_page=page,
    )
    return render(request, "booktest/page_area.html", replace_data)

