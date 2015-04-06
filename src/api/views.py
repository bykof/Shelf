from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from users.models import User
from booking.models import OrderCategory, Article, PaymentMethod, Supplier, Order, InvoiceDocument

from .serializers import OrderCategorySerializer, ArticleSerializer, PaymentMethodSerializer, SupplierSerializer
from .serializers import OrderSerializer, ReadOrderSerializer, UserSerializer, InvoiceDocumentSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (SearchFilter,)
    search_fields = (
        'username',
        'first_name',
        'last_name',
        'email',
    )


class OrderCategoryViewSet(ModelViewSet):
    queryset = OrderCategory.objects.all()
    serializer_class = OrderCategorySerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class PaymentMethodViewSet(ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer


class InvoiceDocumentViewSet(ModelViewSet):
    queryset = InvoiceDocument.objects.all()
    serializer_class = InvoiceDocumentSerializer


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all().order_by('-id')
    paginate_by = 10
    filter_backends = (SearchFilter,)
    search_fields = (
        'bought_by__first_name',
        'bought_by__last_name',
        'bought_by__email',
        'delivery_received_by__first_name',
        'delivery_received_by__last_name',
        'delivery_received_by__email',
        'category__name',
        'article__name',
        'supplier__name',
        'payment_method__name',
        'payment_method__description',
        'order_number',
        'purpose',
        'tags__name',
    )

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


# TODO: create order view for creation of orders and upload of invoice documents