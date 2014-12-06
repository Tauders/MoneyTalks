from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from accounts.models import Account
from categories.models import Category
from places.models import Place
from transactions.models import Transaction


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'transaction-formId'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = '.'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-7'
        self.helper.add_input(Submit('submit', _('Create transaction'), css_class="col-lg-offset-2"))
        self.instance.user = user

        self.fields['account_from'] = forms.ModelChoiceField(queryset=Account.objects.filter(user=user), required=False,
                                                             label=_('From account'))

        self.fields['account_to'] = forms.ModelChoiceField(queryset=Account.objects.filter(user=user), required=False,
                                                           label=_('To account'))

        self.fields['place'] = forms.ModelChoiceField(queryset=Place.objects.filter(user=user), required=False,
                                                      label=_('Place'))

        self.fields['category'] = forms.ModelChoiceField(queryset=Category.objects.filter(user=user), required=False,
                                                         label=_('Category'))
