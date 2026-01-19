from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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


class BookCreateView(CreateView):
    model = Book
    template_name = "library/book_form.html"
    fields = ["title", "author", "year", "style", "publisher", "is_available"]
    success_url = reverse_lazy("library:book_list")


class BookUpdateView(UpdateView):
    model = Book
    template_name = "library/book_form.html"
    fields = ["title", "author", "year", "style", "publisher", "is_available"]
    success_url = reverse_lazy("library:book_list")


class BookDeleteView(DeleteView):
    model = Book
    template_name = "library/book_confirm_delete.html"
    success_url = reverse_lazy("library:book_list")


class ReaderListView(ListView):
    model = Reader
    template_name = "library/reader_list.html"
    context_object_name = "readers"
    ordering = ["last_name", "first_name"]


class ReaderDetailView(DetailView):
    model = Reader
    template_name = "library/reader_detail.html"
    context_object_name = "reader"


class ReaderCreateView(CreateView):
    model = Reader
    template_name = "library/reader_form.html"
    fields = ["first_name", "last_name", "phone", "email"]  
    success_url = reverse_lazy("library:reader_list")


class ReaderUpdateView(UpdateView):
    model = Reader
    template_name = "library/reader_form.html"
    fields = ["first_name", "last_name", "phone", "email"]
    success_url = reverse_lazy("library:reader_list")


class ReaderDeleteView(DeleteView):
    model = Reader
    template_name = "library/reader_confirm_delete.html"
    success_url = reverse_lazy("library:reader_list")
