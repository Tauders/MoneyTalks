#from django.utils.unittest import TestCase
from django.core.exceptions import ValidationError
from django.test import TestCase

from categories.models import Category
from django.contrib.auth import get_user_model


class CategoryTest(TestCase):
    def test_trycategoryname(self):
        user = get_user_model().objects.create(
            username='test',
        )
        cat = Category(name='TestCategory', parent=None, user=user)
        self.assertEqual(cat.__str__(), 'TestCategory')

    def test_cleancategory(self):
        user = get_user_model().objects.create(
            username='test',
        )
        Category.objects.create(name='test', user=user)
        cat2 = Category(name='test', user=user)
        self.assertRaisesMessage(ValidationError, 'Name must be unique', cat2.clean)

    def test_trycategorynamethesameparent(self):
        user = get_user_model().objects.create(
            username='test',
        )
        parent = Category(name='parent', user=user, parent=None)
        Category.objects.create(name='child', user=user, parent=parent)
        child = Category(name='child', user=user, parent=parent)
        self.assertRaisesMessage(ValidationError, 'Name must be unique', child.clean)
