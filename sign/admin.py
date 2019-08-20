from django.contrib import admin

# Register your models here.
from sign.models import Event, Guest

class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'address', 'start_time']
    search_fields = ['name']                                                            #搜索栏
    list_filter = ['status']                                                            #过滤栏
class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone', 'email', 'sign', 'creat_time', 'event']
    search_fields = ['realname', 'phone']  # 搜索栏
    list_filter = ['sign']


admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)