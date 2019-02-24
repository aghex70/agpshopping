from django.test import LiveServerTestCase

from interests.models import Customer, Category

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewCustomerTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        current_user = Customer.objects.get_or_create(name="John", surname="Doe")
        reading_interest, _ = Category.objects.get_or_create(name="reading")
        investing_interest, _ = Category.objects.get_or_create(name="investing")
        traveling_interest, _ = Category.objects.get_or_create(name="traveling")


    def tearDown(self):
        self.browser.quit()


    def check_for_element_in_interests_list(self, element):
        current_interests_list = self.browser.find_element_by_tag_name('ol')
        interests = current_interests_list.find_elements_by_tag_name('li')

        confirmed_interests = [interest.text for interest in interests]
        self.assertIn(element, confirmed_interests,
            f"{element} is not in the interests lists.\n Interests list is: {confirmed_interests}")


    def test_can_save_his_interests(self):
        # John Doe goes to check out this new app he heard by going to its homepage
        self.browser.get(self.live_server_url)

        # He notices that he is on his index page
        self.assertIn('Personal index', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Please select your interests', header_text)

        # He is required to fill in his interests
        investing_checkbox = self.browser.find_element_by_id('id_personal_interests_0')
        traveling_checkbox = self.browser.find_element_by_id('id_personal_interests_2')

        # He checks "investing"
        investing_checkbox.click()
        self.assertIs(investing_checkbox.is_selected(), True)

        # He also checks "traveling"
        traveling_checkbox.click()
        self.assertIs(traveling_checkbox.is_selected(), True)
        # time.sleep(10)

        # When he confirms his interests, the page updates, and now the page shows
        # his interests like a list : "traveling", "investing"
        submit_form_button = self.browser.find_element_by_xpath('/html/body/form/input[2]')
        submit_form_button.click()

        current_user = Customer.objects.get(name="John", surname="Doe")
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(f"{current_user.name}'s interests", header_text)
        # John checks his interests are correctly filled in
        self.check_for_element_in_interests_list('investing')
        self.check_for_element_in_interests_list('traveling')

        self.fail('Test has finished')

    def test_can_save_his_non_existent_interests(self):
        # John Doe goes to check out this new app he heard by going to its homepage
        self.browser.get(self.live_server_url)

        # He notices that he is on his index page
        self.assertIn('Personal index', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text

        # He is asked to fill in his interests, but he doesn't see anything
        # that he enjoys and proceeds without marking any category
        self.assertIn('Please select your interests', header_text)
        submit_form_button = self.browser.find_element_by_xpath('/html/body/form/input[2]')
        submit_form_button.click()

        current_user = Customer.objects.get(name="John", surname="Doe")
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(f"{current_user.name}'s interests", header_text)
        sub_header_text = self.browser.find_element_by_tag_name('h2').text
        # John checks he has no interests filled in
        self.assertIn('There aren\'t any interests selected yet for this user.',
         sub_header_text)

        self.fail('Test has finished')


    # def test_check_were_filled_correctly(self):
    #
    #     self.check_for_element_in_interests_list('investing')
    #     self.check_for_element_in_interests_list('traveling')
    #
    #     self.fail('Test has finished')
