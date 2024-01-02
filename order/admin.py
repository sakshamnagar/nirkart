from django.contrib import admin
from .models import *

# Register your models here.

class Orders(admin.ModelAdmin):
    list_display = ('order_id','status','item_vendor','buyer',)

class Rev(admin.ModelAdmin):
    list_display = ('item','user','rating')

admin.site.register(DeliveryCharges)
admin.site.register(Order, Orders)
admin.site.register(Reviews,Rev)