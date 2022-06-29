# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.test import TestCase

class TestDjango(TestCase):

    def test_this_thing_works(self):
        self.assertEqual(1, 0)

    def test_this_thing_works2(self):
        self.assertEqual(1, 1)