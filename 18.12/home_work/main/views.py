from django.views.generic import ListView, DetailView
from .models import Book, Reader


class BookListView(ListView):
    model = Book
    template_name = "library/book_list.html"
    context_object_name = "books"
    ordering = ["title"]


class BookDetailView(DetailView):
    model = Book
    template_name = "library/book_detail.html"
    context_object_name = "book"


class ReaderListView(ListView):
    model = Reader
    template_name = "library/reader_list.html"
    context_object_name = "readers"
    ordering = ["last_name", "first_name"]


class ReaderDetailView(DetailView):
    model = Reader
    template_name = "library/reader_detail.html"
    context_object_name = "reader"
