from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=80)
    parent = models.ForeignKey('self', null=True, blank=True)
    user = models.ForeignKey(User, related_name='categories')

    def __str__(self):
        return self.name