from django.contrib.auth.models import User
from django.db import models


class Place(models.Model):
  name = models.CharField(max_length=80)
  user = models.ForeignKey(User, related_name='places')

  def __str__(self):
    return self.name