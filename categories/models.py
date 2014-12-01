from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=80)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
    user = models.ForeignKey(User, related_name='categories')

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def clean(self):
        clean_data = super().clean()
        categories = self.user.categories.filter(name=self.name, parent=self.parent)
        if categories.exists():
            raise ValidationError('Name must be unique')
        return clean_data
