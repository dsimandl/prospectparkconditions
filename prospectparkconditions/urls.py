from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'conditions.views.home_page', name='home'),
    url(r'^condition-reports/(\d+)/$', 'conditions.views.view_condition_report', name='view_condition_report'),
    url(r'^condition-reports/(\d+)/add-reports$', 'conditions.views.add_condition_report', name='add_condition_report'),
    url(r'^condition-reports/new$', 'conditions.views.new_condition_report', name='new_condition_report'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
