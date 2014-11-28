from decimal import Decimal
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=80, verbose_name=_('Название счёта'))
    user = models.ForeignKey(User, related_name='accounts')

    def __str__(self):
        return self.name

    def balance(self):
        value = Decimal(0.00)
        for transaction in self.transactions_from.all():
            value -= transaction.amount
        for transaction in self.transactions_to.all():
            value += transaction.amount
        return value

    def clean(self):
        cleaned_data = super().clean()
        if self.user.accounts.filter(name=self.name).exists():
            raise ValidationError(_('Название должно быть уникальным'))
        return cleaned_data
