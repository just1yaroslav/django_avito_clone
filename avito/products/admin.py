from django.contrib import admin

from products.models import ProductModel


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'status', 'title', 'author', 'price']
    list_filter = ['category', 'status', 'title', 'author', 'price']
    search_fields = ['title', 'author', 'price']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'created_at'
    ordering = ['status']

