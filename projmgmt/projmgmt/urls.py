from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'projmgmt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^stories/', include('stories.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
