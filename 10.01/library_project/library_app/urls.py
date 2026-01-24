from django.urls import path
from . import views

app_name = "library"

urlpatterns = [
    path("", views.home, name="home"),
    path("books/", views.BookListView.as_view(), name="book_list"),
    path("books/available/", views.AvailableBookListView.as_view(), name="book_list_available"),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("readers/", views.ReaderListView.as_view(), name="reader_list"),
    path("readers/<int:pk>/", views.ReaderDetailView.as_view(), name="reader_detail"),
]
