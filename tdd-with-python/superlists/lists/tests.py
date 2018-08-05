from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):

        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request=request)

        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'To-Do lists', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

    def test_home_page_can_save_a_post_request(self):
        request = HttpRequest()
        request.method = "POST"
        request.POST["item_text"] = "a new item list"

        response = home_page(request)

        self.assertIn("a new item list", response.content.decode())
