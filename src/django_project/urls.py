from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from adventure_time.api import WorldResource, CharacterResource


admin.autodiscover()

# world_resource = WorldResource()
# character_resource = CharacterResource()
v1_api = Api(api_name='v1')
v1_api.register(WorldResource())
v1_api.register(CharacterResource())

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       (r'^api/', include(v1_api.urls)),
                       # url(r'api/doc/', include('tastypie_swagger.urls', namespace='tastypie_swagger')),
                       url(r'api/v1/doc/',
                          include('tastypie_swagger.urls', namespace='myapi_tastypie_swagger'),
                          kwargs={"tastypie_api_module":"myapp.registration.my_api", "namespace":"myapi_tastypie_swagger"}
                        ),
                       )
