# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.test import TestCase
from blog.models import Category


class TestBlogModels(TestCase):

    def test_model_Category(self):
        name = Category.objects.create(name="Django Testing")
        self.assertNotEqual(name, '')

    def test_category_string_method_returns_name(self):
        name = Category.objects.create(name='test blog name')
        self.assertEqual(str(name), 'test blog name')

    def test_get_absolute_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
