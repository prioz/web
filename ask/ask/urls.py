from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'ask.qa.views.test', name='test'),
    url(r'^login/', 'ask.qa.views.test', name='test'),
    url(r'^signup/', 'ask.qa.views.test', name='test'),
    url(r'^question/[0-9]*?/', 'ask.qa.views.test', name='test'),
    url(r'^ask/', 'ask.qa.views.test', name='test'),
    url(r'^popular/', 'ask.qa.views.test', name='test'),
    url(r'^new/', 'ask.qa.views.test', name='test'),
    url(r'^admin/', include(admin.site.urls)),
)

