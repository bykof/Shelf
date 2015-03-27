from rest_framework.viewsets import ModelViewSet

from booking.models import OrderCategory, Article, PaymentMethod, Supplier, Order

from .serializers import OrderCategorySerializer, ArticleSerializer, PaymentMethodSerializer, SupplierSerializer
from .serializers import OrderSerializer, ReadOrderSerializer


class OrderCategoryViewSet(ModelViewSet):
    queryset = OrderCategory.objects.all()
    serializer_class = OrderCategorySerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class PaymentMethodViewSet(ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()

    def list(self, request, *args, **kwargs):
        return super(OrderViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        Order.objects.get(pk=kwargs['pk']).tags.clear()
        return super(OrderViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        Order.objects.get(pk=kwargs['pk']).tags.clear()
        return super(OrderViewSet, self).update(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReadOrderSerializer
        elif self.request.method == 'POST':
            return OrderSerializer
        else:
            return OrderSerializer