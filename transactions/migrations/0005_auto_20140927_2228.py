# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('places', '0001_initial'),
        ('transactions', '0004_auto_20140922_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(blank=True, to='categories.Category', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='transaction',
            name='place',
            field=models.ForeignKey(blank=True, to='places.Place', null=True),
            preserve_default=True,
        ),
    ]
