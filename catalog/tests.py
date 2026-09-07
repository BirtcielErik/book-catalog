from django.test import TestCase
from django.urls import reverse
from .models import Publisher, Book, Review

class BookListTest(TestCase):
    def test_books_page_contains_title(self):
        # Arrange
        publisher = Publisher.objects.create(name="Random House")
        Book.objects.create(publisher=publisher, title="Theodore Rex", num_pages=772)

        # Act
        response = self.client.get(reverse("book_list"))

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Theodore Rex")