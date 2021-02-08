from django.contrib import admin
# 관리자 페이지 커스텀 
# Register your models here.
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created','updated']
    raw_id_fields = ['author'] # input의 텍스트 타입처럼 입력할 수 있게 만든다.
    list_filter = ['created','updated','author']
    search_fields = ['text','created','author__username']
    # 검색해서 찾을 수 있게 하고 str타입이기 때문에 author는 id 객체이기 때문에 하위의 username이런 식으로 넣어준다.
    ordering = ['-updated','-created']


admin.site.register(Photo, PhotoAdmin)