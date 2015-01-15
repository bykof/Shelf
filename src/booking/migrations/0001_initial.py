# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import taggit.managers
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('bookingmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='booking.BookingModel')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
            ],
            options={
            },
            bases=('booking.bookingmodel',),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('bookingmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='booking.BookingModel')),
                ('bought_on', models.DateTimeField(default=datetime.datetime(2015, 1, 15, 14, 11, 36, 857739))),
                ('purpose', models.CharField(max_length=255, null=True, blank=True)),
                ('order_number', models.CharField(max_length=255)),
                ('delivery_received_on', models.DateTimeField(null=True, blank=True)),
                ('status', models.CharField(max_length=255, choices=[(b'ORDERED', 'Ordered'), (b'WAITING_FOR_DELIVERY', 'Waiting for delivery'), (b'DELIVERY_RECEIVED', 'Delivery received'), (b'CREATED_INVENTORY_ITEM', 'Inventory item was created')])),
                ('invoice_document', models.FileField(upload_to=b'')),
                ('article', models.ForeignKey(related_name='orders', to='booking.Article')),
                ('bought_by', models.ForeignKey(related_name='bought_orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=('booking.bookingmodel',),
        ),
        migrations.CreateModel(
            name='OrderCategory',
            fields=[
                ('bookingmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='booking.BookingModel')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=('booking.bookingmodel',),
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('bookingmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='booking.BookingModel')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=('booking.bookingmodel',),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('bookingmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='booking.BookingModel')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=('booking.bookingmodel',),
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
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
    ]
