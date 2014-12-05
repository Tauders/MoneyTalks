from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.forms import ModelForm

from categories.models import Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.instance.user = user
        self.fields['parent'] = forms.ModelChoiceField(queryset=Category.objects.filter(user=user), required=False)
        self.helper = FormHelper()
        self.helper.form_id = 'place-formId'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = '.'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-7'
        self.instance.user = user
        self.helper.add_input(Submit('submit', ('Создать'), css_class="register-submit"))

