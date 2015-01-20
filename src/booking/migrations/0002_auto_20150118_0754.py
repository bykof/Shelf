# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_squashed_0002_auto_20150115_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='bought_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 18, 7, 54, 19, 239151)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
    ]
