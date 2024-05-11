from django.test import TestCase, Client
from django.urls import reverse
from . import views

class ExampleViewTestCase(TestCase):
    def setUP(self):
        self.client = Client()

    def test_index_GET(self):
        response = self.client.get(reverse("index_page"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        
    def test_get_book_GET(self):
        response = self.client.get(reverse('str_test', args=['Hamlet']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"<h1>Book Hamlet was published in 1603 year.</h1>")
    
    def test_book_post_POST(self):
        response = self.client.post(reverse('book_added'), {'book_title' :'Oliver Twist', 'book_year' : '1838'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/book-added/')

    def test_if_book_is_present(self):
        response = self.client.get(reverse('index_page'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Twist',response.content)