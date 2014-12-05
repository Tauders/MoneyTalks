from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=80, verbose_name=_('Название'))
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', verbose_name=_('Потомки'))
    user = models.ForeignKey(User, related_name='categories', verbose_name=_('Пользователь'))

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def clean(self):
        clean_data = super().clean()
        categories = self.user.categories.filter(name=self.name, parent=self.parent)
        if categories.exists():
            raise ValidationError(_('Имя должно быть уникальным'))
        return clean_data
