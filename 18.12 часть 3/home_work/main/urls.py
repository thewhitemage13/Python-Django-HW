from django.urls import path
from .views import (
    BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView,
    ReaderListView, ReaderDetailView, ReaderCreateView, ReaderUpdateView, ReaderDeleteView
)

app_name = "main"

urlpatterns = [
    path("books/", BookListView.as_view(), name="book_list"),
    path("books/add/", BookCreateView.as_view(), name="book_add"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("books/<int:pk>/edit/", BookUpdateView.as_view(), name="book_edit"),
    path("books/<int:pk>/delete/", BookDeleteView.as_view(), name="book_delete"),
    path("readers/", ReaderListView.as_view(), name="reader_list"),
    path("readers/add/", ReaderCreateView.as_view(), name="reader_add"),
    path("readers/<int:pk>/", ReaderDetailView.as_view(), name="reader_detail"),
    path("readers/<int:pk>/edit/", ReaderUpdateView.as_view(), name="reader_edit"),
    path("readers/<int:pk>/delete/", ReaderDeleteView.as_view(), name="reader_delete"),
]
