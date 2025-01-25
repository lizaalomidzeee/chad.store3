from django.contrib import admin
from.models import Product, ProductTag, Review

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'currency', 'quantity')
    list_filter = ('currency',)
    search_fields = ('name', 'description')
    
    

@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    
    


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'created_at')
    list_filter = ('rating', 'created_at', 'updated_at')
    search_fields = ('user__username', 'product__name', 'content')