from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewCustomerTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

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
        time.sleep(1)
        current_interests_list = self.browser.find_element_by_tag_name('ul').text
        self.assertIn('Currently selected interests', current_interests_list)
        interests = current_interests_list.find_elements_by_tag_name('li')

        self.assertTrue(
            any(row.text == 'Cryptocurrencies' for interest in interests),
            'Cryptocurrencies is not in the interests list')

        self.assertTrue(
            any(row.text == 'Books' for interest in interests),
            'Books is not in the interests list')

        self.fail('Test has finished')


if __name__ == '__main__':
    unittest.main(warnings=None)
