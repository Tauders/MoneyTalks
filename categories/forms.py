from django.forms import ModelForm

from categories.models import Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        exclude = ('user',)