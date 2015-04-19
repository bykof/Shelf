# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_order_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='price',
        ),
        migrations.AddField(
            model_name='order',
            name='article_quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.FloatField(),
        ),
    ]
