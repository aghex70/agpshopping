from django.test import LiveServerTestCase

from interests.models import Customer, Category

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewCustomerTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        Customer.objects.get_or_create(name="John", surname="Doe")
        reading_interest, _ = Category.objects.get_or_create(name="reading")
        investing_interest, _ = Category.objects.get_or_create(name="investing")
        traveling_interest, _ = Category.objects.get_or_create(name="traveling")

    def tearDown(self):
        self.browser.quit()

    def check_for_element_in_interests_list(self, element, list):
        current_interests_list = self.browser.find_element_by_tag_name('ul').text
        interests = current_interests_list.find_elements_by_tag_name('li')
        self.assertIn(element, [interest.text for interest in interests],
            f"{element} is not in the interests lists.\n Interests list is: {confirmed_interests}")



    def test_can_start_to_fill_her_interests(self):
        # She goes to check out this new app she heard by going to its homepage
        self.browser.get(self.live_server_url)
        time.sleep(10)

        # She notices that she is on her index page
        self.assertIn('Personal index', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Please select your interests', header_text)

        # She is required to fill in her interests
        investing_checkbox = self.browser.find_element_by_id('id_personal_interests_0')
        traveling_checkbox = self.browser.find_element_by_id('id_personal_interests_2')

        # She checks "investing"
        investing_checkbox.click()
        self.assertIs(investing_checkbox.is_selected(), True)

        # She also checks "traveling"
        traveling_checkbox.click()
        self.assertIs(traveling_checkbox.is_selected(), True)
        # time.sleep(10)

        # When she confirms her interests, the page updates, and now the page shows
        # her interests like a list : "Cryptocurrencies", "Books"
        submit_form_button = self.browser.find_element_by_xpath('/html/body/form/input[2]')
        submit_form_button.click()

        # self.check_for_element_in_interests_list('reading')
        # self.check_for_element_in_interests_list('traveling')

        self.fail('Test has finished')
