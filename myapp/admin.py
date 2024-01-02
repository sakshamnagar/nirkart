from django.contrib import admin

# Register your models here.
from .models import *

class Sub(admin.ModelAdmin):
    list_display = ('name','slug',)
    list_editable = ('name',)

class Cat(admin.ModelAdmin):
    list_display = ('name','slug')
    list_editable = ('slug',)

class Items(admin.ModelAdmin):
    list_display = ('name','image',)
    list_editable = ('image',)

# Register your models here.
admin.site.register(Item, Items)
admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(MainCategory)
admin.site.register(AdminOffers)
admin.site.register(Banner)
