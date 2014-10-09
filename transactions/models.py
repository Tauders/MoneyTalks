from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from accounts.models import Account
from categories.models import Category
from places.models import Place


class Transaction(models.Model):
    account_from = models.ForeignKey(
        Account, null=True, blank=True,
        related_name='transactions_from'
    )
    account_to = models.ForeignKey(
        Account, null=True, blank=True,
        related_name='transactions_to'
    )
    user = models.ForeignKey(User, null=True, blank=True)
    place = models.ForeignKey(Place, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    datetime = models.DateTimeField(
        default=timezone.now
    )
    comments = models.TextField(
        blank=True
    )

    def __str__(self):
        return '{}: {}, from {} to {}'.format(
            self.datetime,
            self.amount,
            self.account_from,
            self.account_to,
        )

    def clean(self):
        cleaned_data = super().clean()
        if self.account_from == self.account_to:
            raise ValidationError(
                'Accounts must be different'
            )
        return cleaned_data
