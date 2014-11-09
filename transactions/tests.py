# Create your tests here.
from django.db import IntegrityError
from django.test import TestCase
from places.models import Place
from django.contrib.auth import get_user_model
from accounts.models import Account
from transactions.models import Transaction

class TransactionTest(TestCase):
    def test_double_amount(self):
        user = get_user_model().objects.create(
            username='test',
        )
        account1 = Account.objects.create(
            name='test1',
            user=user,
        )
        account2 = Account.objects.create(
            name='test1',
            user=user,
        )
        account1.save()
        account2.save()
        user.save()
        self.assertEqual(account1.name, account2.name)