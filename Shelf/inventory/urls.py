from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns(
	'inventory.views',
	url(
		r'^$',  # noqa
		TemplateView.as_view(template_name='inventory/home.html'),
		name="inventory"
	),
)