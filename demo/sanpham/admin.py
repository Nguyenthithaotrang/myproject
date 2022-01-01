from django.contrib import admin
from .models import sanpham
# Register your models here.
class sanphamAdmin(admin.ModelAdmin):
    list_display = ('sanpham_id', 'danhmucsanpham_id', 'name', 'price', 'anh', 'mota')
    search_fields = ['name']
    list_filter = ('sanpham_id', 'danhmucsanpham_id', 'name', 'price', 'anh', 'mota')
admin.site.register(sanpham, sanphamAdmin)