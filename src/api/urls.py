from rest_framework.routers import DefaultRouter

from .views import OrderCategoryViewSet, ArticleViewSet, PaymentMethodViewSet, SupplierViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'order-categories', OrderCategoryViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'payment-methods', PaymentMethodViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = router.urls