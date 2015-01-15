import datetime

from django.utils.translation import ugettext as _
from django.db import models

from taggit.managers import TaggableManager

from ..users.models import User


class BookingModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class OrderCategory(BookingModel):
    name = models.CharField(max_length=255)


class Article(BookingModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)


class PaymentMethod(BookingModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Supplier(BookingModel):
    name = models.CharField(max_length=255)


class Order(BookingModel):
    ORDERED = 'ORDERED'
    WAITING_FOR_DELIVERY = 'WAITING_FOR_DELIVERY'
    DELIVERY_RECEIVED = 'DELIVERY_RECEIVED'
    CREATED_INVENTORY_ITEM = 'CREATED_INVENTORY_ITEM'

    STATUS_CHOICES = (
        (ORDERED, _('Ordered')),
        (WAITING_FOR_DELIVERY, _('Waiting for delivery')),
        (DELIVERY_RECEIVED, _('Delivery received')),
        (CREATED_INVENTORY_ITEM, _('Inventory item was created'))
    )

    bought_by = models.ForeignKey(User, related_name='bought_orders')
    bought_on = models.DateTimeField(default=datetime.datetime.now())
    category = models.ForeignKey(OrderCategory, related_name='orders')
    article = models.ForeignKey(Article, related_name='orders')
    supplier = models.ForeignKey(Supplier, related_name='orders')
    purpose = models.CharField(null=True, blank=True, max_length=255)
    payment_method = models.ForeignKey(PaymentMethod, related_name='orders')
    order_number = models.CharField(max_length=255)
    delivery_received_on = models.DateTimeField(null=True, blank=True)
    delivery_received_by = models.ForeignKey(User, null=True, blank=True, related_name='received_orders')
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    invoice_document = models.FileField()
    tags = TaggableManager()