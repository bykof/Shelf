from rest_framework import serializers

from users.models import User

from booking.models import Order, OrderCategory, Article, PaymentMethod, \
    Supplier


"""
USER SERIALIZERS
"""


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


"""
BOOKING SERIALIZERS
"""


class OrderCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCategory


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order


class OrderCollapsedSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()
    bought_by = UserSerializer()
    category = OrderCategorySerializer()
    supplier = SupplierSerializer()
    payment_method = PaymentMethodSerializer()
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Order