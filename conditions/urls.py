from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^(\d+)/$', 'conditions.views.view_condition_report', name='view_condition_report'),
    url(r'^(\d+)/add-reports$', 'conditions.views.add_condition_report', name='add_condition_report'),
    url(r'^new$', 'conditions.views.new_condition_report', name='new_condition_report'),
)