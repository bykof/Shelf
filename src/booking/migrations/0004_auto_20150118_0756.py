# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20150118_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='bought_on',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
