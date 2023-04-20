from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title_category",)}
    list_display = ("title_category", "id")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'image',
        'is_active',
        'created',
    )
    list_filter = (
        'is_active',
        'created',
    )
    search_fields = (
        'title',
    )
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 330px;">')