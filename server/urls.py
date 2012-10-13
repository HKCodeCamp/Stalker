import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from google.appengine.dist import use_library
use_library('django', '1.3')

from django.conf.urls.defaults import *

from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
#    (r'^robots\.txt$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'}),
#    (r'^sitemap\.xml$', direct_to_template, {'template': 'sitemap.xml', 'mimetype': 'application/xml'}),
#    (r'^BingSiteAuth\.xml$', direct_to_template, {'template': 'BingSiteAuth.xml', 'mimetype': 'application/xml'}),
#    (r'^googlebd\.html$', direct_to_template, {'template': 'googlebd902ebda634df76.html', 'mimetype': 'text/html'}),
    (r'^', include('stalkerapp.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
