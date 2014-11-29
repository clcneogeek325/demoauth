from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import view_index

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'demoauth.views.view_index', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
