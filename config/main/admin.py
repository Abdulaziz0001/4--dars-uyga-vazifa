from django.contrib import admin

from .models import Color, Brand, Car

# Register your models here.

class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

admin.site.register(Color)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

admin.site.register(Brand)

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'info', 'color')
    list_display_links = ('name',)

admin.site.register(Car)