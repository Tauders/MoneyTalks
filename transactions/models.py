from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from accounts.models import Account
from categories.models import Category
from places.models import Place


class Transaction(models.Model):
    account_from = models.ForeignKey(
        Account, null=True, blank=True,
        related_name='transactions_from',
        verbose_name=_('From account')
    )

    account_to = models.ForeignKey(
        Account, null=True, blank=True,
        related_name='transactions_to',
        verbose_name=_('To account')
    )

    user = models.ForeignKey(User, null=True, blank=True, verbose_name=_('User'))
    place = models.ForeignKey(Place, null=True, blank=True, verbose_name=_('Place'))
    category = models.ForeignKey(Category, null=True, blank=True, verbose_name=_('Category'))

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('Amount')
    )

    datetime = models.DateTimeField(
        default=timezone.now,
        verbose_name=_('Date')
    )

    comments = models.TextField(
        blank=True,
        verbose_name=_('Comment')
    )

    def __str__(self):
        return '{}: {}, from {} to {}'.format(
            self.datetime.strftime("%d.%m.%y %H:%M"),
            self.amount,
            self.account_from,
            self.account_to,
        )

    def clean(self):
        cleaned_data = super().clean()
        if self.account_from == self.account_to:
            raise ValidationError(_('Accounts must differ'))
        return cleaned_data
