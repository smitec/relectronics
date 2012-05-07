from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('basket.views',
	url(r'^$', 'view_basket'),
	url(r'^add/([0-9\-]+)/', 'add_to_basket'),
	url(r'^remove/([0-9\-]+)/', 'remove_from_basket'),
	url(r'^print/$', 'print_view')
)