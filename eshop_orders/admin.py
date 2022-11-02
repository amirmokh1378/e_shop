from django.contrib import admin
from .models import Order, OrderDetail, DiscountSet, Discount
# Register your models here.

admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(DiscountSet)
admin.site.register(Discount)
