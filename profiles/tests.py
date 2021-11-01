from django.test import SimpleTestCase
from django.urls import resolve, reverse
from pyquery import PyQuery

from .views import HomePageView


class HomepageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home:index')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        """check if it's the right Template"""
        self.assertTemplateUsed(self.response, 'profiles/index.html')

    def test_homepage_title(self):
        pq = PyQuery(self.response.content)
        title_scrapped = pq("h1").text()
        title_page = "Homepage"
        assert title_scrapped == title_page

    def test_homepage_url_resolves_index(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__, HomePageView.__name__
        )
