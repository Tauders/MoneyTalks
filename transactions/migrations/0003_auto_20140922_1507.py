# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
        ('transactions', '0002_auto_20140922_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='account_from',
            field=models.ForeignKey(blank=True, to='accounts.Account', null=True, related_name='transactions_from'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='transaction',
            name='account_to',
            field=models.ForeignKey(blank=True, to='accounts.Account', null=True, related_name='transactions_to'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
