from django.conf.urls import patterns, url

urlpatterns = patterns(
    'booking.views',
    url(
        r'^(?P<page>[-\w]+.html)/$',
        'booking',
        name="booking"
    ),
)