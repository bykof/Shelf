from django.contrib.auth import login, authenticate, logout

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

from booking.models import Order, OrderCategory, Article, PaymentMethod, \
    Supplier
from api.serializers import OrderSerializer, OrderCategorySerializer, ArticleSerializer, \
    PaymentMethodSerializer, SupplierSerializer
from api.metadatas import OrderMetadata

"""
LOGIN LOGOUT VIEWS
"""


@api_view(['POST'])
@permission_classes((AllowAny, ))
def login_view(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return Response(200)
            else:
                return Response(401)
        else:
            return Response(403)



@api_view(['GET'])
def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return Response(200)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def is_logged_in(request):
    if request.method == 'GET':
        return Response(not request.user.is_anonymous())


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
    metadata_class = OrderMetadata
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_fields = ('order_number', 'purpose')


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



