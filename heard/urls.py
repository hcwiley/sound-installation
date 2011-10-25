from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.defaults import page_not_found
from django.views.generic.simple import redirect_to, direct_to_template
from heard import settings
admin.autodiscover()

urlpatterns = patterns('',
    (r'^favicon.ico$', redirect_to, {'url': '/site_media/static/images/fav.ico'}),
    (r'^get/(?P<page>.*)/?$', 'views.get'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^$', 'views.default', {'page':'home'}),
#    (r'^home$', page_not_found),
    (r'^robots.txt$', direct_to_template, {'template':'robots.txt', 'mimetype':'text/plain'}),
    (r'^sitemap.txt$', direct_to_template, {'template':'sitemap.txt', 'mimetype':'text/plain'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^admin$', redirect_to, {'url': '/admin/'}),
    
)

urlpatterns += patterns('',
        (r'%s(?P<path>.*)$' % settings.AUDIO_URL, 'django.views.static.serve', {'document_root': settings.AUDIO_ROOT}),
        (r'%s(?P<path>.*)$' % settings.GALLERY_URL, 'django.views.static.serve', {'document_root': settings.GALLERY_ROOT}),
        (r'^%s*/(?P<path>.*)$' % settings.STATIC_URL, 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

#Login
urlpatterns += patterns('',
    (r'^login$', 'views.login'),
    (r'^logout$', 'views.logout'),
)

urlpatterns += patterns('',
    (r'^add-piece$', 'views.add_piece'),
    (r'^save-street$', 'views.save_street'),
    (r'^save-location$', 'views.save_location'),
    (r'^edit$', 'views.edit', {'page':'home'}),
    (r'^edit/$', 'views.edit', {'page':'home'}),
    (r'^edit/(?P<page>.*)$', 'views.edit'),
    (r'^(?P<page>.*)$', 'views.default'), # make sure this is last as it will catch everything
)
