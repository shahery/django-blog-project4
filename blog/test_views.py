# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.test import TestCase

class TestViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)  

    def test_get_post_detail_page(self):
        response = self.client.get('/post_detail')
        self.assertEqual(response.status_code, 301)

    def test_can_post_like(self):
        response = self.client.get('/post_like')
        self.assertEqual(response.status_code, 301)

    def test_can_add_post(self):
        response = self.client.get('/add_post')
        self.assertEqual(response.status_code, 301)

    def test_can_add_category(self):
        response = self.client.get('/add_category')
        self.assertEqual(response.status_code, 301)

    def test_get_edit_post_page(self):
        response = self.client.get('/edit_post/99')
        self.assertEqual(response.status_code, 404)

    def test_can_delete_post(self):
        response = self.client.get('/delete_post')
        self.assertEqual(response.status_code, 301)

    def test_get_category_page(self):
        response = self.client.get('/category')
        self.assertEqual(response.status_code, 301)
        