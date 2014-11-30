# Create your tests here.
from django.core.exceptions import ValidationError
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
        # Transaction.objects.create(account_from='test', account_to='test', user=user)
        acc = Account(name='qwe', user=user)
        acc.save()
        trans2 = Transaction(account_from=acc, account_to=acc, user=user)
        self.assertRaisesMessage(ValidationError, 'Счета должны быть разные', trans2.clean)
