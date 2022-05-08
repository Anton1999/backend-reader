from django.contrib import admin

from .models import Book, Genre, Chapter, Rate

class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'status', 'photo']


admin.site.register(Genre,  GenreAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Chapter)
admin.site.register(Rate)
