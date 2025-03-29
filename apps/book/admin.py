from django.contrib import admin
from apps.book.models import Book
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author']
    search_fields = ['id', 'name', 'author']
    list_filter = ['id', 'name', 'author']