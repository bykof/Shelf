from rest_framework.serializers import ModelSerializer

from users.models import User
from booking.models import OrderCategory, Article, PaymentMethod, Supplier, Order


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


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


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order


class ReadOrderSerializer(ModelSerializer):
    bought_by = UserSerializer()
    category = OrderCategorySerializer()
    article = ArticleSerializer()
    supplier = SupplierSerializer()
    payment_method = PaymentMethodSerializer()

    class Meta:
        model = Order

