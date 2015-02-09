from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    'api.views',

    # LOGIN LOGOUT URLS
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^is-logged-in/$', views.is_logged_in, name='is_logged_in'),

    # BOOKING URLS

    url(r'^order-categories/$', views.OrderCategoryList.as_view(), name='order_category_list'),
    url(r'^order-categories/(?P<pk>[0-9]+)$', views.OrderCategoryDetail.as_view(), name='order_category_detail'),

    url(r'^articles/$', views.ArticleList.as_view(), name='article_list'),
    url(r'^articles/(?P<pk>[0-9]+)$', views.ArticleDetail.as_view(), name='article_detail'),

    url(r'^payment-methods/$', views.PaymentMethodList.as_view(), name='payment_method_list'),
    url(r'^order-categories/(?P<pk>[0-9]+)$', views.PaymentMethodDetail.as_view(), name='payment_method_detail'),

    url(r'^suppliers/$', views.SupplierList.as_view(), name='supplier_list'),
    url(r'^suppliers/(?P<pk>[0-9]+)$', views.SupplierDetail.as_view(), name='supplier_detail'),

    url(r'^orders/$', views.OrderList.as_view(), name='order_list'),
    url(r'^orders-collapsed/$', views.OrderListCollapsed.as_view(), name='order_list_collapsed'),
    url(r'^orders/(?P<pk>[0-9]+)$', views.OrderDetail.as_view(), name='order_detail'),

)