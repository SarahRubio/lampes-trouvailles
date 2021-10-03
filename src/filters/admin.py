from django import forms
from django.contrib import admin

from filters.models import Category, SubCategory, Color, Designer, Material, State, Style


class SubCategoryAdmin(admin.ModelAdmin):

    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
    fields = [
        'name', 'slug', 'description', 'category'
    ]
    search_fields = ['name']
    list_filter = ['name']


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
    fields = [
        'name', 'slug', 'short_description',
    ]
    search_fields = ['name']
    list_filter = ['name']



class ColorAdmin(admin.ModelAdmin):

    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
    fields = [
        'name', 'slug', 'code'
    ]
    search_fields = ['name']
    list_filter = ['name']


class DesignerAdmin(admin.ModelAdmin):

    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
    fields = [
        'name', 'slug', 'description'
    ]
    search_fields = ['name']
    list_filter = ['name']


class MaterialAdmin(admin.ModelAdmin):

    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
    fields = [
        'name', 'slug', 'description'
    ]
    search_fields = ['name']
    list_filter = ['name']


class StateAdmin(admin.ModelAdmin):

    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
    fields = [
        'name', 'slug'
    ]
    search_fields = ['name']
    list_filter = ['name']


class StyleAdmin(admin.ModelAdmin):

    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
    fields = [
        'name', 'slug', 'description'
    ]
    search_fields = ['name']
    list_filter = ['name']


admin.site.register(Style, StyleAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Designer, DesignerAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Category, CategoryAdmin)