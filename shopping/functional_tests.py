from selenium import webdriver
import unittest

class NewCustomerTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_to_fill_her_interests(self):
        # She goes to check out this new app she heard by going to its homepage
        self.browser.get('http://localhost:8000')

        # She notices that she is on the interests fill in page
        self.assertIn('Customer interests', self.browser.title)
        self.fail('Finishing the test')

if __name__ == '__main__':
    unittest.main(warnings=None)
