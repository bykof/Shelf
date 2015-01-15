from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.views',
    url(r'^orders/$', 'order_list', name='order_list'),
    url(r'^orders/(?P<pk>[0-9]+)$', 'order_detail', name='order_detail'),
)