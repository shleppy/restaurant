from django.contrib import admin

from restaurant.models import Category, Customer, Item


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'type']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'date')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description',
                    'category', 'slug']
