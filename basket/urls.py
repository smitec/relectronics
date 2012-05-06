from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('basket.views',
	url(r'^/$', 'view_basket'),
	url(r'^add/(?:)')
)