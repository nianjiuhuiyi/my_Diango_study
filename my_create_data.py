"""
    这仅仅是用来初始化类，创造数据好写一些,这里不可以直接运行的，要去 python manage.py shell里
"""
from datetime import date
from booktest.models import BookInfo

b = BookInfo()
b.btitle = "天龙八部"
b.bpub_date = date(1990, 1, 1)  # 注意使用的date的数据格式
b.save()  # 因为继承了django.db中的models.Model，执行save就是操作数据库

print(BookInfo.objects.all())