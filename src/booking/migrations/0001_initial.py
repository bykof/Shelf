# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import taggit.managers
from django.conf import settings
import booking.models


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
            bases=(models.Model, booking.models.BookingModel),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bought_on', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('purpose', models.CharField(max_length=255, null=True, blank=True)),
                ('order_number', models.CharField(max_length=255)),
                ('delivery_received_on', models.DateTimeField(null=True, blank=True)),
                ('status', models.CharField(default=b'ORDERED', max_length=255, choices=[(b'ORDERED', 'Ordered'), (b'WAITING_FOR_DELIVERY', 'Waiting for delivery'), (b'DELIVERY_RECEIVED', 'Delivery received'), (b'CREATED_INVENTORY_ITEM', 'Inventory item was created')])),
                ('invoice_document', models.FileField(null=True, upload_to=b'', blank=True)),
                ('article', models.ForeignKey(related_name='orders', to='booking.Article')),
                ('bought_by', models.ForeignKey(related_name='bought_orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
            bases=(models.Model, booking.models.BookingModel),
        ),
        migrations.CreateModel(
            name='OrderCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Order category',
                'verbose_name_plural': 'Order categories',
            },
            bases=(models.Model, booking.models.BookingModel),
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Payment method',
                'verbose_name_plural': 'Payment methods',
            },
            bases=(models.Model, booking.models.BookingModel),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Suppliers',
            },
            bases=(models.Model, booking.models.BookingModel),
        ),
        migrations.AddField(
            model_name='order',
            name='category',
            field=models.ForeignKey(related_name='orders', to='booking.OrderCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_received_by',
            field=models.ForeignKey(related_name='received_orders', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.ForeignKey(related_name='orders', to='booking.PaymentMethod'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='supplier',
            field=models.ForeignKey(related_name='orders', to='booking.Supplier'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
    ]
