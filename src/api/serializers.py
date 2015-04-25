from rest_framework.serializers import ModelSerializer, DateTimeField, CharField

from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer

from users.models import User
from booking.models import OrderCategory, Article, PaymentMethod, Supplier, Order, InvoiceDocument, OrderItem


"""
CUSTOM SERIALIZER
"""


"""
USER SERIALIZER
"""


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


"""
BOOKING SERIALIZER
"""


class OrderCategorySerializer(ModelSerializer):
    class Meta:
        model = OrderCategory


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article


class PaymentMethodSerializer(ModelSerializer):
    class Meta:
        model = PaymentMethod


class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier


class OrderSerializer(TaggitSerializer, ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Order


class InvoiceDocumentSerializer(ModelSerializer):
    invoice_file_filename = CharField(required=False)
    order = OrderSerializer()

    class Meta:
        model = InvoiceDocument

class OrderItemSerializer(ModelSerializer):
    order = OrderSerializer()
    article = ArticleSerializer()

    class Meta:
        model = OrderItem

class ReadOrderSerializer(ModelSerializer):
    bought_by = UserSerializer()
    delivery_received_by = UserSerializer()
    category = OrderCategorySerializer()
    supplier = SupplierSerializer()
    payment_method = PaymentMethodSerializer()
    tags = TagListSerializerField()
    invoice_documents = InvoiceDocumentSerializer(many=True)

    class Meta:
        model = Order
