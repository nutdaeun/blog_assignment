from django.contrib import admin
from .models import Blog # Blog 모델을 admin 사이트에 등록하기 위해 import

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',) # date 필드를 읽기 전용으로 설정하여 수정할 수 없도록 함

admin.site.register(Blog, BlogAdmin) # Blog 모델을 admin 사이트에 등록하여 관리할 수 있도록 설정