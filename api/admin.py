from django.contrib import admin

# Register your models here.
from .models import Student  # 记得导包


@admin.register(Student)
class BlogTypeAdmin(admin.ModelAdmin):
    # 在后台列表下显示的字段
    list_display = ('pk', 'name')
