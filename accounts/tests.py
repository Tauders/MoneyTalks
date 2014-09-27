from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase

from accounts.models import Account
from transactions.models import Transaction


class TransactionTest(TestCase):
  def test_balance(self):
    amount = Decimal(1.23)
    user = get_user_model().objects.create(
      username='test',
    )
    account = Account.objects.create(
      name='test',
      user=user,
    )
    Transaction.objects.create(
      account_to=account,
      amount=amount,
    )
    self.assertAlmostEqual(account.balance(), amount, 2)

