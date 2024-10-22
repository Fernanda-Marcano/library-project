from django.contrib import admin
from .models import Author, Category, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'biography']
    list_filter = ('name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_year', 'author', 'category']
    list_filter = ('title', 'author', 'category', 'pub_year')
    date_hierarchy = ('pub_year')

admin.site.register(Author, AuthorAdmin)

admin.site.register(Category)

admin.site.register(Book, BookAdmin)