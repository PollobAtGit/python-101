from django.test import TestCase
from django.urls import resolve
from lists.views import home_page, home_page_index


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):

        found = resolve('/')
        self.assertEqual(found.func, home_page)
        self.assertEqual(found.func(), "i am from home page")

        self.fail("complete implementation")
