from django.contrib import admin
from .models import Book, Reader, Borrow

admin.site.register(Book)
admin.site.register(Reader)
admin.site.register(Borrow)
