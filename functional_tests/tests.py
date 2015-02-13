from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_condition_report_and_retrieve_it_later(self):
        # Sally has heard about a cool new online prospect park condition reporting app.  She goes to checkout its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention prospect park conditions
        self.assertIn('Prospect Park', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Prospect Park', header_text)

        # She is invited to enter a condition report right away
        date_time_input = self.browser.find_element_by_id('id_new_date_time')
        self.assertEqual(date_time_input.get_attribute('placeholder'), 'Enter the date and time of the report')
        road_condition_input = self.browser.find_element_by_id('id_new_road_condition')
        self.assertEqual(road_condition_input.get_attribute('placeholder'), 'Enter a road condition for the report')
        weather_input = self.browser.find_element_by_id('id_new_weather_report')
        self.assertEqual(weather_input.get_attribute('placeholder'), 'Enter the weather with the report')
        crowds_input = self.browser.find_element_by_id('id_new_crowds_report')
        self.assertEqual(crowds_input.get_attribute('placeholder'), 'Enter the crowd condition with the report')
        notes_input = self.browser.find_element_by_id('id_new_report_notes')
        self.assertEqual(notes_input.get_attribute('placeholder'), 'Enter any notes with the report')
        submit_button = self.browser.find_element_by_id('id_submit_button')

        # She types in the date and time of the report (02/12/2015 12:00PM)
        date_time_input.send_keys('02/12/2015 12:00PM')
        # She types in condition of the road (Mostly Dry, some ice on the access roads)
        road_condition_input.send_keys('Mostly Dry, some ice on the access roads')
        # She types in the weather for the report (Cold, cloudy with some flurries)
        weather_input.send_keys('Cold, cloudy with some flurries')
        # She types in if it was crowded (Not crowded, only a handful of other runners.  No bikes today)
        crowds_input.send_keys('Not crowded, only a handful of other runners. No bikes today')
        # She types in other notes that she has for the report (The park overall is in good shape for a run!  The snow makes it look great!)
        notes_input.send_keys('The park overall is in good shape for a run! The snow makes it look great!')

        # When she hits enter, the page updates, and now the page lists
        submit_button.send_keys(Keys.ENTER)
        # - 02/12/2015 12:00PM as the date, "Mostly Dry, some ice on the access roads" as the road condition,

        #   "Cold, cloudy with some flurries" as the weather, "Not crowded, only a handful of other runners.  No bikes today",
        #   "The park overall is in good shape for a run!  The snow makes it look great!"
        table = self.browser.find_element_by_id('id_condition_report_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('02/12/2015 12:00PM', [row.text for row in rows])
        self.assertIn('Mostly Dry, some ice on the access roads', [row.text for row in rows])
        self.assertIn('Cold, cloudy with some flurries', [row.text for row in rows])
        self.assertIn('Not crowded, only a handful of other runners. No bikes today', [row.text for row in rows])
        self.assertIn('The park overall is in good shape for a run! The snow makes it look great!', [row.text for row in rows])


        # There are text boxes inviting her to enter another park condition report.

        # She types in the date and time of the report (06/25/2015 06:00PM)
        # She types in condition of the road (The road is slick and sloppy from the rain early this afternoon)
        # She types in the weather for the report (Muggy, warm, and sunny)
        # She types in if it was crowded (Very crowded! Lots of pedestrians and bikes!)
        # She types in other notes that she has for the report (Be aware there is a celebrate brooklyn show tonight!
        #   The park drives are full of pedestrians and bikes, especially by the bandshell)

        # When she hits enter there are two condition reports listed.  The first one and this one:
          # - 06/25/2015 06:00PM as the date, "The road is slick and sloppy from the rain early this afternoon" as the road condition,
        #   "Muggy, warm, and sunny" as the weather, "Very crowded! Lots of pedestrians and bikes!" as the crowds,
        #   "Be aware there is a celebrate brooklyn show tonight!
        #   The park drives are full of pedestrians and bikes, especially by the bandshell"