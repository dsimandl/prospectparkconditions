from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from conditions.views import home_page
from conditions.models import ConditionReport

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['new_date_time'] = '01/01/2014 3:00PM'
        request.POST['new_road_condition'] = 'Great'
        request.POST['new_weather_report'] = 'Awesome'
        request.POST['new_crowds_report'] = 'Terrible'
        request.POST['new_report_notes'] = 'Blah Blah'

        response = home_page(request)

        self.assertEqual(ConditionReport.objects.count(), 1)
        new_object = ConditionReport.objects.first()
        self.assertEqual(new_object.date_time, '01/01/2014 3:00PM')
        self.assertEqual(new_object.road_condition, 'Great')
        self.assertEqual(new_object.weather_report, 'Awesome')
        self.assertEqual(new_object.crowds_report, 'Terrible')
        self.assertEqual(new_object.report_notes, 'Blah Blah')

    def test_home_page_redirects_after_POST(self):

        request = HttpRequest()
        request.method = 'POST'
        request.POST['new_date_time'] = '01/01/2014 3:00PM'
        request.POST['new_road_condition'] = 'Great'
        request.POST['new_weather_report'] = 'Awesome'
        request.POST['new_crowds_report'] = 'Terrible'
        request.POST['new_report_notes'] = 'Blah Blah'

        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_home_page_displays_all_list_items(self):
        ConditionReport.objects.create(date_time='01/01/2014 3:00PM',
                                       road_condition='Great',
                                       weather_report='Awesome',
                                       crowds_report='Terrible',
                                       report_notes='Blah Blah')

        ConditionReport.objects.create(date_time='01/02/2014 3:00PM',
                                       road_condition='Ok',
                                       weather_report='Cold!',
                                       crowds_report='Noone',
                                       report_notes='HeHe')

        request = HttpRequest()
        response = home_page(request)

        self.assertIn('01/01/2014 3:00PM', response.content.decode())
        self.assertIn('01/02/2014 3:00PM', response.content.decode())

class ConditionReportModelTest(TestCase):

    def test_saving_and_retrieving_reports(self):
        first_report = ConditionReport()
        first_report.date_time = '01/01/2014 1:00PM'
        first_report.road_condition = 'Great'
        first_report.weather_report = 'Awesome'
        first_report.crowds_report = 'Terrible'
        first_report.report_notes = 'Blah Blah'
        first_report.save()

        second_report = ConditionReport()
        second_report.date_time = '01/02/2014 1:00PM'
        second_report.road_condition = 'Terrible'
        second_report.weather_report = 'Cold'
        second_report.crowds_report = 'Great'
        second_report.report_notes = 'Empty!'
        second_report.save()

        saved_reports = ConditionReport.objects.all()
        self.assertEqual(saved_reports.count(), 2)

        first_saved_report = saved_reports[0]
        second_saved_report = saved_reports[1]

        self.assertEqual(first_saved_report.date_time, '01/01/2014 1:00PM')
        self.assertEqual(first_saved_report.road_condition, 'Great')
        self.assertEqual(first_saved_report.weather_report, 'Awesome')
        self.assertEqual(first_saved_report.crowds_report, 'Terrible')
        self.assertEqual(first_saved_report.report_notes, 'Blah Blah')

        self.assertEqual(second_saved_report.date_time, '01/02/2014 1:00PM')
        self.assertEqual(second_saved_report.road_condition , 'Terrible')
        self.assertEqual(second_saved_report.weather_report, 'Cold')
        self.assertEqual(second_saved_report.crowds_report, 'Great')
        self.assertEqual(second_saved_report.report_notes, 'Empty!')

    def test_home_page_only_saves_reports_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(ConditionReport.objects.count(), 0)
