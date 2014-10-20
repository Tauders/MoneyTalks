from django.forms import ModelForm

from accounts.models import Account


class AccountForm(ModelForm):
    class Meta:
        model = Account
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(AccountForm, self).__init__(*args, **kwargs)
        self.instance.user = user