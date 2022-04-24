from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()

    def __str__(self):
        return self.btitle

    class Meta:
        db_table = "bookinfo"


# 人物类
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=128)
    # 关系属性 hbook 简历图书类和人物类之间的一对多关系（这很关键）
    # 它的格式就会是  hbook_id  # 会自己加一个_id
    hbook = models.ForeignKey("BookInfo", on_delete=models.CASCADE)   # 外键，类名别写错了

    def __str__(self):
        return self.hname  # 为了页面显示人物的名字，而不是一个 “HerInfo object(number)” 这种

    class Meta:
        db_table = "heroinfo"
