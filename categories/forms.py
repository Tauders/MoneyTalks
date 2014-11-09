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
