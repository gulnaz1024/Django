from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display=['title', 'price','updated','timestamp']
    list_display_links=['price']
    list_filter=['updated','timestamp']
    search_fields=['price','description']

admin.site.register(Product,ProductAdmin)
