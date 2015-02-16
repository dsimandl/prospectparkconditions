from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def get_intput_box_and_send_keys(self, element_id, text):
        input_box = self.browser.find_element_by_id(element_id)
        self.assertEqual(input_box.get_attribute('placeholder'), text)
        return input_box

    def send_keys(self, input_box, text_to_send):
        input_box.send_keys(text_to_send)

    def check_for_row_in_list_table(self, row_text, element='id_condition_report_table' ):
        table = self.browser.find_element_by_id(element)
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_condition_report_and_retrieve_it_later(self):
        # Sally has heard about a cool new online prospect park condition reporting app.  She goes to checkout its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention prospect park conditions
        self.assertIn('Prospect Park', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Prospect Park', header_text)

        # She is invited to enter a condition report right away

        date_time_input = self.get_intput_box_and_send_keys('id_new_date_time', 'Enter the date and time of the report')
        road_condition_input = self.get_intput_box_and_send_keys('id_new_road_condition', 'Enter a road condition for the report')
        weather_input = self.get_intput_box_and_send_keys('id_new_weather_report', 'Enter the weather with the report')
        crowds_input = self.get_intput_box_and_send_keys('id_new_crowds_report', 'Enter the crowd condition with the report')
        notes_input = self.get_intput_box_and_send_keys('id_new_report_notes', 'Enter any notes with the report')
        submit_button = self.browser.find_element_by_id('id_submit_button')

        # She types in the date and time of the report (02/12/2015 12:00PM)
        self.send_keys(date_time_input, '02/12/2015 12:00PM')
        # She types in condition of the road (Mostly Dry, some ice on the access roads)
        self.send_keys(road_condition_input, 'Mostly Dry, some ice on the access roads')
        # She types in the weather for the report (Cold, cloudy with some flurries)
        self.send_keys(weather_input, 'Cold, cloudy with some flurries')
        # She types in if it was crowded (Not crowded, only a handful of other runners.  No bikes today)
        self.send_keys(crowds_input, 'Not crowded, only a handful of other runners. No bikes today')
        # She types in other notes that she has for the report (The park overall is in good shape for a run!  The snow makes it look great!)
        self.send_keys(notes_input, 'The park overall is in good shape for a run! The snow makes it look great!')

        # When she hits enter, the page updates, and now the page lists
        submit_button.send_keys(Keys.ENTER)
        # - 02/12/2015 12:00PM as the date, "Mostly Dry, some ice on the access roads" as the road condition,

        #   "Cold, cloudy with some flurries" as the weather, "Not crowded, only a handful of other runners.  No bikes today",
        #   "The park overall is in good shape for a run!  The snow makes it look great!"
        self.check_for_row_in_list_table('02/12/2015 12:00PM')
        self.check_for_row_in_list_table('Mostly Dry, some ice on the access roads')
        self.check_for_row_in_list_table('Cold, cloudy with some flurries')
        self.check_for_row_in_list_table('Not crowded, only a handful of other runners. No bikes today')
        self.check_for_row_in_list_table('The park overall is in good shape for a run! The snow makes it look great!')

        # There are text boxes inviting her to enter another park condition report.

        date_time_input = self.get_intput_box_and_send_keys('id_new_date_time', 'Enter the date and time of the report')
        road_condition_input = self.get_intput_box_and_send_keys('id_new_road_condition', 'Enter a road condition for the report')
        weather_input = self.get_intput_box_and_send_keys('id_new_weather_report', 'Enter the weather with the report')
        crowds_input = self.get_intput_box_and_send_keys('id_new_crowds_report', 'Enter the crowd condition with the report')
        notes_input = self.get_intput_box_and_send_keys('id_new_report_notes', 'Enter any notes with the report')
        submit_button = self.browser.find_element_by_id('id_submit_button')

        # She types in the date and time of the report (06/25/2015 06:00PM)
        self.send_keys(date_time_input, '06/25/2015 6:00PM')
        # She types in condition of the road (The road is slick and sloppy from the rain early this afternoon)
        self.send_keys(road_condition_input, 'The road is slick and sloppy from the rain early this afternoon')
        # She types in the weather for the report (Muggy, warm, and sunny)
        self.send_keys(weather_input, 'Muggy, warm, and sunny')
        # She types in if it was crowded (Very crowded! Lots of pedestrians and bikes!)
        self.send_keys(crowds_input, 'Very crowded! Lots of pedestrians and bikes!')
        # She types in other notes that she has for the report (Be aware there is a celebrate brooklyn show tonight!
        #   The park drives are full of pedestrians and bikes, especially by the bandshell)
        self.send_keys(notes_input, 'Be aware there is a celebrate brooklyn show tonight! The park drives are full of pedestrians and bikes, especially by the bandshell')

        # When she hits enter there are two condition reports listed.
        submit_button.send_keys(Keys.ENTER)
        # The first one:
        self.check_for_row_in_list_table('02/12/2015 12:00PM')
        self.check_for_row_in_list_table('Mostly Dry, some ice on the access roads')
        self.check_for_row_in_list_table('Cold, cloudy with some flurries')
        self.check_for_row_in_list_table('Not crowded, only a handful of other runners. No bikes today')
        self.check_for_row_in_list_table('The park overall is in good shape for a run! The snow makes it look great!')
        # and this one:
        self.check_for_row_in_list_table('06/25/2015 6:00PM')
        self.check_for_row_in_list_table('The road is slick and sloppy from the rain early this afternoon')
        self.check_for_row_in_list_table('Muggy, warm, and sunny')
        self.check_for_row_in_list_table('Very crowded! Lots of pedestrians and bikes!')
        self.check_for_row_in_list_table('Be aware there is a celebrate brooklyn show tonight! The park drives are full of pedestrians and bikes, especially by the bandshell')

          # - 06/25/2015 06:00PM as the date, "The road is slick and sloppy from the rain early this afternoon" as the road condition,
        #   "Muggy, warm, and sunny" as the weather, "Very crowded! Lots of pedestrians and bikes!" as the crowds,
        #   "Be aware there is a celebrate brooklyn show tonight!
        #   The park drives are full of pedestrians and bikes, especially by the bandshell"