from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import Book

class BookModelTests(TestCase):
    def test_string_representation(self):
        book = Book(title="Django Testing")
        self.assertEqual(str(book), book.title)

class BookViewTests(TestCase):
    def setUp(self):
        Book.objects.create(title="Django for Beginners", author="William S. Vincent")
        Book.objects.create(title="Two Scoops of Django", author="Daniel Roy Greenfeld")

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Django for Beginners")
        self.assertContains(response, "Two Scoops of Django")
        self.assertTemplateUsed(response, 'myapp/book_list.html')


