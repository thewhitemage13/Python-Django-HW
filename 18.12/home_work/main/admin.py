from django.contrib import admin
from .models import Book, Reader

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "year", "publisher", "style", "is_available")
    list_filter = ("publisher", "style", "year", "is_available")
    search_fields = ("title", "author", "publisher", "style")


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone", "email", "joined_at")
    search_fields = ("first_name", "last_name", "email", "phone")
