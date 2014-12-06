from crispy_forms.layout import Submit
from django import forms
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper

from places.models import Place


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(PlaceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'place-formId'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = '.'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-7'
        self.instance.user = user
        self.helper.add_input(Submit('submit', _('Create place'), css_class="register-submit"))
