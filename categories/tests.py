from django.utils.unittest import TestCase
# from django.test import TestCase

from categories.models import Category
from django.contrib.auth import get_user_model


class CategoryTest(TestCase):
    def test_trycategory(self):
        cat = Category()
        cat.parent = None
        cat.name = 'TestCategory'
        user = get_user_model().objects.create(
            username='test',
        )
        cat.user = user
        self.assertEqual(cat.__str__(), 'TestCategory')
