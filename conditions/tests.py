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

class ConditionReportViewTest(TestCase):

    def test_uses_conditionreport_template(self):
        response = self.client.get('/condition-reports/the-only-report-in-the-world/')
        self.assertTemplateUsed(response, 'condition_report.html')

    def test_displays_all_items(self):
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

        response = self.client.get('/condition-reports/the-only-report-in-the-world/')

        self.assertContains(response, '01/01/2014 3:00PM')
        self.assertContains(response, '01/02/2014 3:00PM')

class NewConditionReportTest(TestCase):

    def test_saving_a_POST_request(self):
        self.client.post(
            '/condition-reports/new',
            data={'new_date_time': '01/01/2014 3:00PM',
                  'new_road_condition': 'Great',
                  'new_weather_report': 'Awesome',
                  'new_crowds_report': 'Terrible',
                  'new_report_notes' : 'Blah Blah'}
        )

        self.assertEqual(ConditionReport.objects.count(), 1)
        new_object = ConditionReport.objects.first()
        self.assertEqual(new_object.date_time, '01/01/2014 3:00PM')
        self.assertEqual(new_object.road_condition, 'Great')
        self.assertEqual(new_object.weather_report, 'Awesome')
        self.assertEqual(new_object.crowds_report, 'Terrible')
        self.assertEqual(new_object.report_notes, 'Blah Blah')

    def test_redirects_after_POST(self):
        response = self.client.post(
            '/condition-reports/new',
            data={'new_date_time': '01/01/2014 3:00PM',
                  'new_road_condition': 'Great',
                  'new_weather_report': 'Awesome',
                  'new_crowds_report': 'Terrible',
                  'new_report_notes' : 'Blah Blah'}
        )

        self.assertRedirects(response, '/condition-reports/the-only-report-in-the-world/')