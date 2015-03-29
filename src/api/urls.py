from django.conf.urls import url

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import OrderCategoryViewSet, ArticleViewSet, PaymentMethodViewSet, SupplierViewSet, OrderViewSet
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'order-categories', OrderCategoryViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'payment-methods', PaymentMethodViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = router.urls
urlpatterns += [
    url(r'^api-token-auth/', views.obtain_auth_token)
]