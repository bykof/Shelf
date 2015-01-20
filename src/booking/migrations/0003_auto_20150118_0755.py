# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20150118_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='bought_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 18, 7, 55, 27, 45911)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default=b'ORDERED', max_length=255, choices=[(b'ORDERED', 'Ordered'), (b'WAITING_FOR_DELIVERY', 'Waiting for delivery'), (b'DELIVERY_RECEIVED', 'Delivery received'), (b'CREATED_INVENTORY_ITEM', 'Inventory item was created')]),
            preserve_default=True,
        ),
    ]
