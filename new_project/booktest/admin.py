from django.contrib import admin

# Register your models here.
from booktest.models import BookInfo, HeroInfo

class BookInfoAdmin123(admin.ModelAdmin):
    list_display = ["id", "btitle", "bpub_date"]


class HeroInfoAdmin123(admin.ModelAdmin):
    list_display = ["hname", "hgender", "hcomment", "hbook"]


admin.site.register(BookInfo, BookInfoAdmin123)  # 可能不会有智能提示，写就对了
admin.site.register(HeroInfo, HeroInfoAdmin123)  # 注册人物类
