from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from interests.models import Customer
from interests.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

    def test_homepage_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        # Customer creation in order to fill interests
        Customer.objects.create(name="Alberto", surname="Garcia")

        response = self.client.post('/',
         data={
         'reading': False,
         'traveling': True,
         'investing': True,
         })
        print(response.content.decode())

        new_customer = Customer.objects.first()
        customer_interests = [category.name for category in new_customer.interests.all()]

        self.assertNotIn('reading', customer_interests)
        self.assertIn('travelling', customer_interests)
        self.assertIn('investing', customer_interests)

    def test_redirects_after_POST(self):
        # Customer creation in order to fill interests
        Customer.objects.create(name="Alberto", surname="Garcia")

        response = self.client.post('/',
         data={
         'reading': False,
         'traveling': True,
         'investing': True,
         })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, '/user/interests')
