from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Book, Reader


def home(request):
    return render(request, "home.html")


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"
    paginate_by = 20
    ordering = ["title"]


class AvailableBookListView(BookListView):
    template_name = "books/book_list_available.html"

    def get_queryset(self):
        # книги без активної видачі
        return Book.objects.exclude(borrows__returned_at__isnull=True).order_by("title")


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"


# Доступ до читачів тільки користувачам НЕ з групи readers (або з окремими правами)
class ReaderListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "library_app.view_reader"
    model = Reader
    template_name = "readers/reader_list.html"
    context_object_name = "readers"
    paginate_by = 20
    ordering = ["last_name", "first_name"]


class ReaderDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "library_app.view_reader"
    model = Reader
    template_name = "readers/reader_detail.html"
    context_object_name = "reader"
