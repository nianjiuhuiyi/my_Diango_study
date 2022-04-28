from django.db import models

# Create your models here.

from django.db.models import Q
class MyBookInfoManager(models.Manager):
    """自定义图书管理器类"""
    # 重写继承下来的all()方法
    def all(self):
        # 1.调用父类的all()方法，获取所有的数据
        books = super().all()     # 得到QuerySet
        # 2.对数据进行自定义处理，再返回
        books = books.filter(Q(btitle__contains='猪') | Q(bpub_date__lt="2022-04-01"))
        return books

    # 新建一个自定义方法，用来创建新的图书数据
    def my_create(self, name, date):
        # new_book = BookInfo()  # 万一下面的类名改变了，这就错了
        Class_name = self.model  # 继承下来的"model"属性能拿到其所在类的名字
        new_book = Class_name()    # 实例化
        new_book.btitle = name
        new_book.bpub_date = date  # 日期可以是一个格式比较好的字符串，不是非得datetime.date(1997, 10, 12)
        new_book.save()
        return new_book    # 给一个返回值，也方便在创建时直接拿到这个新建的对象


# 设计和表对应的类，模型类
# 图书类
# (1)一定要继承 models.Model 这个类，两个类属性就是表的字段
class BookInfo(models.Model):
    # (2)图书名称：CharField说明是一个字符串，有最大长度
    btitle = models.CharField(max_length=20)
    # (3)出版日期：DateField说明是一个日期类型
    bpub_date = models.DateField()

    # models.manager.Manager和models.Manager()是一模一样的,都可以
    # 自定义Manager()类
    objects = MyBookInfoManager()  # 为了统一，就还是取名为objects

    def __str__(self):
        return self.btitle   # 为了页面显示书名

    class Meta:
        db_table = "bookinfo"


# 人物类
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    # 性别，用的布尔值，有一个默认值False
    hgender = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=128)
    # 关系属性 hbook 简历图书类和人物类之间的一对多关系（这很关键）
    # 它的格式就会是  hbook_id  # 会自己加一个_id
    hbook = models.ForeignKey("BookInfo", on_delete=models.CASCADE)   # 外键，类名别写错了
    # 1.8就不是必须给on_delete，参数解释看这 https://blog.csdn.net/vivian_wanjin/article/details/84068821
    # https://www.jianshu.com/p/c3550f2d2d4d

    def __str__(self):
        return self.hname  # 为了页面显示人物的名字，而不是一个 “HerInfo object(number)” 这种

    class Meta:
        db_table = "heroinfo"


class PicTest(models.Model):
    """上传图片"""
    # 代表放在static/media/booktest这个目录下，注意相对路径写法
    goods_pic = models.ImageField(upload_to="booktest")
    # 新加类后，重新迁移后，大抵会得到这养一个提示“No migrations to apply.”

    class Meta:
        db_table = "pictures"
