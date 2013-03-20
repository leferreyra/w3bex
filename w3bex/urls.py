from django.conf.urls.defaults import patterns, include, url
from w3bex import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'w3bex.views.home', name='home'),
    # url(r'^w3bex/', include('w3bex.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # w3bex urls
    url(r'^$', 'blog.views.index'),
    url(r'^blog/$', 'blog.views.post_list'),
    url(r'^blog/(\S+)/$', 'blog.views.post'),
)


# servir archivos estaticos en servidor de desarrollo
if settings.DEBUG:
    urlpatterns += patterns('', 
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
	    'document_root': settings.MEDIA_ROOT,}),
        )
