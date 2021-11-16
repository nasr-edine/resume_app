from django.test import TestCase, override_settings
from django.urls import resolve, reverse
from pyquery import PyQuery

from resume_app.settings import MEDIA_ROOT
from .models import Skill
from .models import CustomUser
from .views import HomePageView
from django.core.files.uploadedfile import SimpleUploadedFile
import os
import tempfile
import shutil

image_path = os.path.join(MEDIA_ROOT, 'avatar')
image_path = os.path.join(image_path, '0.jpeg')

document_path = os.path.join(MEDIA_ROOT, 'cv')
document_path = os.path.join(document_path, 'dummy.pdf')
MEDIA_ROOT = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class HomepageTests(TestCase):
    def setUp(self):
        image = SimpleUploadedFile(name='test_image.jpg', content=open(
            image_path, 'rb').read(), content_type='image/jpeg')

        resume = SimpleUploadedFile(name='test_resume.pdf', content=open(
            document_path, 'rb').read(), content_type='application/pdf')
        # print(resume)
        self.user1 = CustomUser.objects.create(
            username="johndoo", first_name="john", last_name="doo", email="johndoo@mail.com", avatar=image, cv=resume)
        # print(self.user1.cv.name)
        # print(self.user1.cv.path)
        # print(self.user1.cv.url)
        self.skill1 = Skill.objects.create(name="heroku", score=50, is_key_skill=False)

        self.user1.skills.add(self.skill1)

        self.user1 = CustomUser.objects.get(first_name="john")
        self.skill1 = Skill.objects.get(name="heroku")

        url = reverse('home:index')
        self.response = self.client.get(url)

    def tearDown(self):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)

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
        self.assertEqual(self.user1.avatar.name, "avatar/test_image.jpg")
        self.assertEqual(self.user1.avatar.url, "/media/avatar/test_image.jpg")
        self.assertEqual(self.user1.cv.name, "cv/test_resume.pdf")
        self.assertEqual(self.user1.cv.url, "/media/cv/test_resume.pdf")

    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        """check if it's the right Template"""
        self.assertTemplateUsed(self.response, 'profiles/index.html')

    def test_homepage_content(self):
        pq = PyQuery(self.response.content)
        img = pq(".bannerUserImg img")
        cv = pq(".bannerBtnCol a").eq(0)
        # assert pq("h1").text() == "Hi, I'm John"
        assert img.attr('alt') == "John Doo avatar"
        assert img.attr('src') == "/media/avatar/test_image.jpg"
        assert cv.attr('href') == "/media/cv/test_resume.pdf"

    def test_homepage_url_resolves_index(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__, HomePageView.__name__
        )
