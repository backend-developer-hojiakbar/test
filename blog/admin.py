from django.contrib import admin
from .models import News, Products, Gallery, Comment, Sotuv
# Register your models here.
admin.site.register(News)
admin.site.register(Gallery)
admin.site.register(Sotuv)
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'created_time', 'active']
    list_filter = ['active', 'created_time']
    search_fields = ['user', 'body']
    actions = ['disable_comments', 'active_commments']

    def disable_comments(self, request, queryset):
        queryset.update(active=False)
    def active_commments(self, request, queryset):
        queryset.update(active=True)