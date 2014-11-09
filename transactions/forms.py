from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm

from transactions.models import Transaction


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'transaction-formId'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = '.'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-7'
        self.helper.add_input(Submit('submit', 'Создать', css_class="col-lg-offset-2"))