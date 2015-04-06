# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import booking.models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20150405_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceDocument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('invoice_file', models.FileField(upload_to=b'invoices')),
                ('order', models.ForeignKey(related_name='invoice_documents', to='booking.Order')),
            ],
            options={
            },
            bases=(models.Model, booking.models.BookingModel),
        ),
        migrations.RemoveField(
            model_name='order',
            name='invoice_document',
        ),
    ]
