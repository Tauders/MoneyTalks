# Create your tests here.
from django.db import IntegrityError
from django.test import TestCase

from places.models import Place


class PlaceTest(TestCase):
    def test_null_place(self):
        with self.assertRaises(IntegrityError):
            p = Place()
            p.save()

    def test_place_without_user(self):
        with self.assertRaises(IntegrityError):
            p = Place.objects.create(
                name='test',
            )
            p.save()

