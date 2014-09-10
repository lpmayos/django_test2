from django.conf.urls import patterns, include, url
from django.contrib import admin
from adventure_time.api import v1_api

admin.autodiscover()


urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       (r'^api/', include(v1_api.urls)),
                       # url(r'api/doc/', include('tastypie_swagger.urls', namespace='tastypie_swagger')),
                       url(r'api/v1/doc/',
                          include('tastypie_swagger.urls', namespace='tastypie_swagger'),
                          kwargs={"tastypie_api_module": "adventure_time.api.v1_api", "namespace": "tastypie_swagger"}
                        ),
                       )
