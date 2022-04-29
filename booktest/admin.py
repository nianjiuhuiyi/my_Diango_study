from django.contrib import admin
from booktest.models import BookInfo, HeroInfo, PicTest, AreaInfo

# Register your models here.

# 这是第一版简单的
# admin.site.register(BookInfo)  # 可能不会有智能提示，写就对了
# admin.site.register(HeroInfo)  # 注册人物类


# 以后就用这种
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "btitle", "bpub_date"]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["hname", "hgender", "hcomment", "hbook"]


class AreaInfoAdmin(admin.ModelAdmin):
    # list_display = ["pid", "dis_name", "level"]  # 这也是可以的
    list_display = ["id", "pid", "dis_name", "level"]  # 这id是自动生成的属性
    list_per_page = 50
    list_filter = ["level"]
    search_fields = ["dis_name"]


admin.site.register(BookInfo, BookInfoAdmin)  # 可能不会有智能提示，写就对了
admin.site.register(HeroInfo, HeroInfoAdmin)  # 注册人物类

admin.site.register(PicTest)  # 注册记录文件上传信息的类

admin.site.register(AreaInfo, AreaInfoAdmin)  # 地区信息表
