from django.contrib import admin
from .models import Products
# Register your models here.
class Product(admin.ModelAdmin):
    list_display = ('id','name')
admin.site.register(Products,Product)
