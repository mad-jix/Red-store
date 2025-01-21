from django.contrib import admin
from .models import Order,CartItems

# Register your models here.


admin.site.register(Order)
admin.site.register(CartItems)