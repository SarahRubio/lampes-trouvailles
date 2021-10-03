from django import forms
from django.contrib import admin

from objects.models import Light, Finding, Furniture


class LightAdmin(admin.ModelAdmin):

    list_display = ['name', 'reference']
    prepopulated_fields = {'slug': ('name',)}
    fields = [
        'name', 'slug', 'reference', 'description', 'first_image',
        'price', 'is_negotiable', 'state',
        'designer', 'categories', 'style', 'materials',
        'colors', 'weight', 'height', 'width', 'depth',
        'is_outstanding', 'is_hightlighted',
    ]
    search_fields = ['name']
    list_filter = [
        'name', 'is_outstanding', 'is_hightlighted',
        'is_negotiable', 'designer', 'categories',
        'style', 'materials'
    ]


class FurnitureAdmin(admin.ModelAdmin):

    list_display = ['name', 'reference']
    prepopulated_fields = {'slug': ('name',)}
    fields = [
        'name', 'slug', 'reference', 'description', 'first_image',
        'price', 'is_negotiable', 'state',
        'designer', 'categories', 'style', 'materials',
        'colors', 'weight', 'height', 'width', 'depth',
        'is_outstanding', 'is_hightlighted',
    ]
    search_fields = ['name']
    list_filter = [
        'name', 'is_outstanding', 'is_hightlighted',
        'is_negotiable', 'designer', 'categories',
        'style', 'materials'
    ]


class FindingAdmin(admin.ModelAdmin):

    list_display = ['name', 'reference']
    prepopulated_fields = {'slug': ('name',)}
    fields = [
        'name', 'slug', 'reference', 'description', 'first_image',
        'price', 'is_negotiable', 'state',
        'designer', 'categories', 'style', 'materials',
        'colors', 'weight', 'height', 'width', 'depth',
        'is_outstanding', 'is_hightlighted',
    ]
    search_fields = ['name']
    list_filter = [
        'name', 'is_outstanding', 'is_hightlighted',
        'is_negotiable', 'designer', 'categories',
        'style', 'materials'
    ]


admin.site.register(Light, LightAdmin)
admin.site.register(Furniture, FurnitureAdmin)
admin.site.register(Finding, FindingAdmin)
