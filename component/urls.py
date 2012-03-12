from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('component.views',
	url(r'^suppliers/$', 'suppliers'),
	url(r'^supplier/(?P<sup_id>\d+)/$', 'supplier'),
	url(r'^(?P<p_id>\d+)/$', 'component'),
	url(r'^search/$', 'search'),
#	url(r'^(?P<poll_id>\d+)/$', 'detail'),
#	url(r'^(?P<poll_id>\d+)/results/$', 'results'),
#	url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)