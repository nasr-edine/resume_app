from django.test import TestCase
from django.urls import resolve, reverse
from pyquery import PyQuery
from .models import Skill
from .models import CustomUser
from .views import HomePageView


class HomepageTests(TestCase):

    def setUp(self):
        self.user1 = CustomUser.objects.create(
            username="johndoo", first_name="john", last_name="doo", email="johndoo@mail.com")

        self.skill1 = Skill.objects.create(name="heroku", score=50, is_key_skill=False)

        self.user1.skills.add(self.skill1)

        self.user1 = CustomUser.objects.get(first_name="john")
        self.skill1 = Skill.objects.get(name="heroku")

        url = reverse('home:index')
        self.response = self.client.get(url)

    def test_skill_is_created(self):
        """skill is created"""
        self.assertEqual(self.skill1.name, "heroku")
        self.assertEqual(self.skill1.score, 50)
        self.assertEqual(self.skill1.is_key_skill, False)

    def test_profile_is_created(self):
        """Profile is created"""
        self.assertEqual(self.user1.username, "johndoo")
        self.assertEqual(self.user1.first_name, "john")
        self.assertEqual(self.user1.last_name, "doo")
        self.assertEqual(self.user1.email, "johndoo@mail.com")
        self.assertEqual(self.user1.skills.all()[0].name, "heroku")

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
