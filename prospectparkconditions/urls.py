from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'conditions.views.home_page', name='home'),
    url(r'^conditionreports/the-only-report-in-the-world/$', 'conditions.views.view_conditionreport')
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
