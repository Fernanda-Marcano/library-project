from django.contrib import admin
from .models import Autor, Category, Book


class AutorAdmin(admin.ModelAdmin):
    fields = ['id','name', 'last_name', 'biography']
    filter_vertical = ['id', 'name', 'last_name']
    list_display = ['name', 'last_name', 'biography']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_year', 'autor', 'category']
    list_filter = ['title', 'autor', 'category', 'pub_year']
    date_hierarchy = ['pub_year']

admin.site.register(Autor, AutorAdmin)

admin.site.register(Category)

admin.site.register(Book, BookAdmin)