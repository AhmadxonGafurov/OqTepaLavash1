from django.contrib import admin

# Register your models here.
from .models import Category,Product,Branche
@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    list_display=('name','image','status')
    list_filter=('status',)
    search_fields=('name',)

@admin.register(Product)
class Product_Admin(admin.ModelAdmin):
    list_display=('name','category','price','status')
    list_filter=('status',)
    search_fields=('name',)

@admin.register(Branche)
class Brange_Admin(admin.ModelAdmin):
    list_display=('name','image','status','address','close_open')
    list_filter=('status',)
    search_fields=('name','created_on')

