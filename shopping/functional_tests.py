from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewCustomerTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def check_for_element_in_interests_list(self, element, list):
        current_interests_list = self.browser.find_element_by_tag_name('ul').text
        interests = current_interests_list.find_elements_by_tag_name('li')
        self.assertIn(element, [interest.text for interest in interests],
            f"{element} is not in the interests lists.\n Interests list is: {confirmed_interests}")



    def test_can_start_to_fill_her_interests(self):
        # She goes to check out this new app she heard by going to its homepage
        self.browser.get('http://localhost:8000')

        # She notices that she is on her index page
        self.assertIn('Personal index', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Please select your interests', header_text)

        # She is required to fill in her interests
        cryptocurrency_checkbox = self.browser.find_element_by_id('id_cryptocurrencies')
        book_checkbox = self.browser.find_element_by_id('id_books')

        # She checks "cryptocurrencies"
        cryptocurrency_checkbox.click()
        self.assertIs(cryptocurrency_checkbox.is_selected(), True)

        # She also checks "books"
        book_checkbox.click()
        self.assertIs(book_checkbox.is_selected(), True)

        # When she confirms her interests, the page updates, and now the page shows
        # her interests like a list : "Cryptocurrencies", "Books"
        submit_form_button = self.browser.find_element_by_xpath('/html/body/form/input[4]')
        submit_form_button.click()
        time.sleep(10)

        self.check_for_element_in_interests_list('Cryptocurrencies')
        self.check_for_element_in_interests_list('Books')

        self.fail('Test has finished')


if __name__ == '__main__':
    unittest.main(warnings=None)
