from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=80)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='parent')
    user = models.ForeignKey(User, related_name='categories')

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def clean(self):
        clean_data = super().clean()
        if self.user.categories.filter(name=self.name, parent=self.parent).exists():
            raise ValidationError('Name must be unique')
        return clean_data

