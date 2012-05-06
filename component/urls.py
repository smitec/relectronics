from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('component.views',
	url(r'^suppliers/$', 'suppliers'),
	url(r'^supplier/(?P<sup_id>\d+)/$', 'supplier'),
	url(r'^(?P<p_id>\d+)/$', 'component'),
	url(r'^search/(?P<page>\d+)/$', 'search'),
	url(r'^search/$', 'search'),
	url(r'^(?P<p_num>[0-9\-]+)/$', 'component')
)