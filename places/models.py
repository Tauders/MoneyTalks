from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=80, verbose_name=_('Place name'))
    user = models.ForeignKey(User, related_name='places')

    def __str__(self):
        return self.name

    def clean(self):
        cleaned_data = super().clean()
        if self.user.places.filter(name=self.name).exists():
            raise ValidationError(_('Name must be unique'))
        return cleaned_data
