from django.contrib import admin
from unicodedata import category

from  .models import Category,News
# Register your models here.
admin.site.register(Category)
admin.site.register(News)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','slug','category','published_time','status']
    list_filter = ['status','published_time','created_time']
    prepopulated_fields = {'slug':('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['']
    ordering = ('titile',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields = ['name']