from django.contrib import admin
from .models import danhmucsanpham
# Register your models here.
class danhmucsanphamAdmin(admin.ModelAdmin):
    list_display = ('danhmucsanpham_id', 'name')
    search_fields = ['name']
    list_filter = ('danhmucsanpham_id', 'name')
admin.site.register(danhmucsanpham,danhmucsanphamAdmin)