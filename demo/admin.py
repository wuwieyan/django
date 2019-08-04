from django.contrib import admin
from demo.models import BookInfo, HeroInfo


# 自定义模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']
    """图书模型管理类"""


# 注册模型类

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)