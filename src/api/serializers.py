from rest_framework import serializers

from booking.models import Order, OrderCategory, Article, PaymentMethod, \
    Supplier


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