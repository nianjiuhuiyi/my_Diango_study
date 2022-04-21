from django.contrib import admin
from booktest.models import BookInfo, HeroInfo

# Register your models here.

# 这是第一版简单的
# admin.site.register(BookInfo)  # 可能不会有智能提示，写就对了
# admin.site.register(HeroInfo)  # 注册人物类

# 以后就用这种
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "btitle", "bpub_date"]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["hname", "hgender", "hcomment", "hbook"]


admin.site.register(BookInfo, BookInfoAdmin)  # 可能不会有智能提示，写就对了
admin.site.register(HeroInfo, HeroInfoAdmin)  # 注册人物类
