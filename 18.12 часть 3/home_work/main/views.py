from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Book, Reader

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "library/book_list.html"
    context_object_name = "books"
    ordering = ["title"]


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = "library/book_detail.html"
    context_object_name = "book"


class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    template_name = "library/book_form.html"
    fields = ["title", "author", "year", "style", "publisher", "is_available"]
    success_url = reverse_lazy("main:book_list")
    permission_required = "main.add_book"


class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    template_name = "library/book_form.html"
    fields = ["title", "author", "year", "style", "publisher", "is_available"]
    success_url = reverse_lazy("main:book_list")
    permission_required = "main.change_book"


class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = "library/book_confirm_delete.html"
    success_url = reverse_lazy("main:book_list")
    permission_required = "main.delete_book"


class ReaderListView(LoginRequiredMixin, ListView):
    model = Reader
    template_name = "library/reader_list.html"
    context_object_name = "readers"
    ordering = ["last_name", "first_name"]


class ReaderDetailView(LoginRequiredMixin, DetailView):
    model = Reader
    template_name = "library/reader_detail.html"
    context_object_name = "reader"


class ReaderCreateView(PermissionRequiredMixin, CreateView):
    model = Reader
    template_name = "library/reader_form.html"
    fields = ["first_name", "last_name", "phone", "email"]
    success_url = reverse_lazy("main:reader_list")
    permission_required = "main.add_reader"


class ReaderUpdateView(PermissionRequiredMixin, UpdateView):
    model = Reader
    template_name = "library/reader_form.html"
    fields = ["first_name", "last_name", "phone", "email"]
    success_url = reverse_lazy("main:reader_list")
    permission_required = "main.change_reader"


class ReaderDeleteView(PermissionRequiredMixin, DeleteView):
    model = Reader
    template_name = "library/reader_confirm_delete.html"
    success_url = reverse_lazy("main:reader_list")
    permission_required = "main.delete_reader"
