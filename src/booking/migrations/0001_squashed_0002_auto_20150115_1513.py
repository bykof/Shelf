# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    replaces = [(b'booking', '0001_initial'), (b'booking', '0002_auto_20150115_1513')]

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
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='ordercategory',
            options={'verbose_name': 'Order category', 'verbose_name_plural': 'Order categories'},
        ),
        migrations.AlterModelOptions(
            name='paymentmethod',
            options={'verbose_name': 'Payment method', 'verbose_name_plural': 'Payment methods'},
        ),
        migrations.AlterModelOptions(
            name='supplier',
            options={'verbose_name': 'Supplier', 'verbose_name_plural': 'Suppliers'},
        ),
        migrations.AlterField(
            model_name='order',
            name='bought_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 15, 15, 13, 15, 678006)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='invoice_document',
            field=models.FileField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
