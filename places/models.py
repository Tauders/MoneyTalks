from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=80, verbose_name=_('Название места'))
    user = models.ForeignKey(User, related_name='places')

    def __str__(self):
        return self.name
