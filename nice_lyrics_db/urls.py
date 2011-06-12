from django.conf.urls.defaults import patterns, include, url
from music import urls as music_urls

urlpatterns = patterns('',
    url(r'^$', include(music_urls)),

)
