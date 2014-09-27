# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
  dependencies = [
    ('transactions', '0001_initial'),
  ]

  operations = [
    migrations.AlterField(
      model_name='transaction',
      name='comments',
      field=models.TextField(blank=True),
    ),
  ]
