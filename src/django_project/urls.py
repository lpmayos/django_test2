from django.conf.urls import patterns, include, url
from django.contrib import admin
from adventure_time.api import WorldResource, CharacterResource

world_resource = WorldResource()
character_resource = CharacterResource()

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       (r'^api/', include(world_resource.urls)),
                       (r'^api/', include(character_resource.urls)),
                       )
