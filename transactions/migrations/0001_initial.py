# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):
  dependencies = [
  ]

  operations = [
    migrations.CreateModel(
      name='Transaction',
      fields=[
        ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
        ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
        ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
        ('comments', models.TextField()),
      ],
      options={
      },
      bases=(models.Model,),
    ),
  ]
