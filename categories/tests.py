#from django.utils.unittest import TestCase
from django.test import TestCase

from categories.models import Category
from django.contrib.auth import get_user_model


class CategoryTest(TestCase):
    def test_trycategoryname(self):
        cat = Category()
        cat.parent = None
        cat.name = 'TestCategory'
        user = get_user_model().objects.create(
            username='test',
        )
        cat.user = user
        self.assertEqual(cat.__str__(), 'TestCategory')

    def test_cleancategory(self):
        user = get_user_model().objects.create(
            username='test',
        )
        cat1 = Category()
        cat1.name='test'
        cat1.user = user
        cat2 = Category()
        cat2.name='test'
        cat2.user = user
        self.assertEqual(Category.clean(cat2), 'Name must be unique')

