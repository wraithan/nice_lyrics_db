from django.conf.urls.defaults import patterns, include, url
import music

urlpatterns = patterns('',
    url(r'^$', include(music.urls)),

)
