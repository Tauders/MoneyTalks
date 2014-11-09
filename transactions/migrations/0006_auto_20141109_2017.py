# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('transactions', '0005_auto_20140927_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='account_from',
            field=models.ForeignKey(verbose_name='Со счёта', null=True, blank=True, to='accounts.Account',
                                    related_name='transactions_from'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='account_to',
            field=models.ForeignKey(verbose_name='На счёт', null=True, blank=True, to='accounts.Account',
                                    related_name='transactions_to'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(verbose_name='Сумма', decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(verbose_name='Категория', null=True, blank=True, to='categories.Category'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='comments',
            field=models.TextField(verbose_name='Комментарий', blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='datetime',
            field=models.DateTimeField(verbose_name='Дата', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='place',
            field=models.ForeignKey(verbose_name='Место', null=True, blank=True, to='places.Place'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(verbose_name='Пользователь', null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
