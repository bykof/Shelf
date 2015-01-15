from rest_framework import serializers

from booking.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order