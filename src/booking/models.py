import os
import datetime

from django.utils.translation import ugettext as _
from django.db import models

from taggit.managers import TaggableManager

from users.models import User


class BookingModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OrderCategory(BookingModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = _('Order category')
        verbose_name_plural = _('Order categories')

    def __unicode__(self):
        return u'{}'.format(self.name)


class Article(BookingModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    def __unicode__(self):
        return u'{} - {}'.format(self.name, self.price)


class PaymentMethod(BookingModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = _('Payment method')
        verbose_name_plural = _('Payment methods')

    def __unicode__(self):
        return u'{} - {}'.format(self.name, self.description[:20])


class Supplier(BookingModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = _('Supplier')
        verbose_name_plural = _('Suppliers')

    def __unicode__(self):
        return u'{}'.format(self.name)


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
    bought_on = models.DateTimeField(default=datetime.datetime.now, blank=True)
    category = models.ForeignKey(OrderCategory, related_name='orders')
    article = models.ForeignKey(Article, related_name='orders')
    supplier = models.ForeignKey(Supplier, related_name='orders')
    purpose = models.CharField(null=True, blank=True, max_length=255)
    payment_method = models.ForeignKey(PaymentMethod, related_name='orders')
    order_number = models.CharField(max_length=255)
    delivery_received_on = models.DateTimeField(null=True, blank=True)
    delivery_received_by = models.ForeignKey(User, null=True, blank=True, related_name='received_orders')
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=ORDERED)
    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    @property
    def get_tags(self, *args, **kwargs):
        return self.tags.filter(*args, **kwargs)

    def __unicode__(self):
        return _(u'Article {} bought on {}'.format(self.article, self.bought_on))


class InvoiceDocument(BookingModel):
    order = models.ForeignKey(Order, related_name='invoice_documents')
    invoice_file = models.FileField(upload_to='invoices')

    @property
    def invoice_file_filename(self):
        return os.path.basename(self.invoice_file.name)

    def __unicode__(self):
        return 'Order: {} - Datei: {}'.format(
            self.order_id,
            self.invoice_file.name
        )