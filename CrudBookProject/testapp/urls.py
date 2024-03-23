from django.urls import path
from .views import createBook, GetAllBooks, GetBookById, GetBookByTitle, update_book, DeleteBookById, DeleteBookByTitle, DeleteAllBooks

urlpatterns = [
    path('book/', createBook, name='create-book'),
    path('books/', GetAllBooks, name='get-all-books'),
    path('book/<int:pk>/', GetBookById, name='get-book-by-id'),
    path('book/title/<str:title>/', GetBookByTitle, name='get-book-by-title'),
    path('book/update/<int:pk>/', update_book, name='update-book'),
    path('book/delete/<int:pk>/', DeleteBookById, name='delete-book-by-id'),
    path('book/delete/title/<str:title>/', DeleteBookByTitle, name='delete-book-by-title'),
    path('books/delete/all/', DeleteAllBooks, name='delete-all-books'),
]
