from django.contrib import admin
from .models import Author, Topic, Poem

admin.site.register(Author)
admin.site.register(Topic)
admin.site.register(Poem)
