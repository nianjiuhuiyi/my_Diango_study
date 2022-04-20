from django.db import models

# Create your models here.

# 设计和表对应的类，模型类
# 图书类
# (1)一定要继承 models.Model 这个类，两个类属性就是表的字段
class BookInfo(models.Model):
    # (2)图书名称：CharField说明是一个字符串，有最大长度
    btitle = models.CharField(max_length=20)
    # (3)出版日期：DateField说明是一个日期类型
    bpub_date = models.DateField()


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
