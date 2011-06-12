from django.conf.urls.defaults import patterns, include, url
from views import home


urlpatterns = patterns('',
    url(r'^$', home, name='home'),

)
