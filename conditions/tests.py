from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from conditions.views import home_page

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
