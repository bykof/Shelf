from rest_framework import generics

from booking.models import Order, OrderCategory, Article, PaymentMethod, \
    Supplier
from api.serializers import OrderSerializer, OrderCategorySerializer, ArticleSerializer, \
    PaymentMethodSerializer, SupplierSerializer


"""
BOOKING CLASS BASED VIEWS
"""


class OrderCategoryList(generics.ListCreateAPIView):
    queryset = OrderCategory.objects.all()
    serializer_class = OrderCategorySerializer


class OrderCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderCategory.objects.all()
    serializer_class = OrderCategorySerializer


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class PaymentMethodList(generics.ListCreateAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer


class PaymentMethodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer


class SupplierList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_fields = ('order_number', 'purpose')


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



