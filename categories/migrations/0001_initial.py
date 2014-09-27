# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('parent', models.ForeignKey(blank=True, to='categories.Category', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='categories')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
