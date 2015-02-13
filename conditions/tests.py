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
        self.assertIn('01/01/2014 3:00PM', response.content.decode())
        self.assertIn('Great', response.content.decode())
        self.assertIn('Awesome', response.content.decode())
        self.assertIn('Terrible', response.content.decode())
        self.assertIn('Blah Blah', response.content.decode())
        expected_html = render_to_string('home.html', {'new_date_time_text': '01/01/2014 3:00PM',
                                                       'new_road_condition_text': 'Great',
                                                       'new_weather_report_text': 'Awesome',
                                                       'new_crowds_report_text': 'Terrible',
                                                       'new_report_notes_text': 'Blah Blah'})
        self.assertEqual(response.content.decode(), expected_html)


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
