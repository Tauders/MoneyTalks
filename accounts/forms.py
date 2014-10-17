from django.forms import ModelForm

from accounts.models import Account


class AccountForm(ModelForm):
    class Meta:
        model = Account
        exclude = ('user',)
