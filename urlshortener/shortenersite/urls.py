from django.conf.urls import patterns, include, url
 
urlpatterns = patterns('shortenersite.views',
    url(r'^$', 'index', name='home'),
    # for our home/index page
 
    url(r'^(?P<short_id>\w{6})$', 'redirect_original', name='redirectoriginal'),
    # when short URL is requested it redirects to original URL
 
    url(r'^makeshort/$', 'shorten_url', name='shortenurl'),
    # this will create a URL's short id and return the short URL
)