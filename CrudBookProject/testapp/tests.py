from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book

class BookTests(APITestCase):
    def setUp(self):
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'publication_date': '2023-01-01',
            'pages': 200,
            'genre': 'Test Genre'
        }
        self.book = Book.objects.create(**self.book_data)

    def test_create_book(self):
        url = reverse('create-book')
        response = self.client.post(url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_books(self):
        url = reverse('get-all-books')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_book_by_id(self):
        url = reverse('get-book-by-id', kwargs={'pk': self.book.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_book_by_title(self):
        url = reverse('get-book-by-title', kwargs={'title': 'Test'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        url = reverse('update-book', kwargs={'pk': self.book.pk})
        updated_data = {
            'title': 'Updated Test Book'
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book_by_id(self):
        url = reverse('delete-book-by-id', kwargs={'pk': self.book.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_book_by_title(self):
        url = reverse('delete-book-by-title', kwargs={'title': 'Test'})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


