from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'relectronics.views.home', name='home'),
    # url(r'^relectronics/', include('relectronics.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^parts/', include('component.urls')),
	url(r'^basket/', include('basket.urls')),
	url(r'^users/', include('users.urls')),
	url(r'^$', direct_to_template, {'template':'base.html'})
)
