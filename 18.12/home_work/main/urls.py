from django.urls import path
from .views import (
    BookListView, BookDetailView,
    ReaderListView, ReaderDetailView
)

app_name = "library"

urlpatterns = [
    path("books/", BookListView.as_view(), name="book_list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book_detail"),

    path("readers/", ReaderListView.as_view(), name="reader_list"),
    path("readers/<int:pk>/", ReaderDetailView.as_view(), name="reader_detail"),
]
