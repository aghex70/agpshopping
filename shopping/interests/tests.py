from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from interests.models import Customer
from interests.models import Category

from interests.forms import InterestsForm

from interests.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

    def test_homepage_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    # def test_forms(self):
    #     form_data = {'reading': False,
    #     'investing': True,
    #     'traveling': True}
    #     form = InterestsForm(data=form_data)
    #     self.assertTrue(form.is_valid())

    def test_can_save_a_POST_request(self):
        Customer.objects.get_or_create(name="John", surname="Doe")
        reading_interest, _ = Category.objects.get_or_create(name="reading")
        investing_interest, _ = Category.objects.get_or_create(name="investing")
        traveling_interest, _ = Category.objects.get_or_create(name="traveling")

        post_data = {'personal_interests': [str(investing_interest.id),
         str(traveling_interest.id)]}

        response = self.client.post('/',
        data=post_data)

        new_customer = Customer.objects.first()
        customer_interests = [category.name for category in new_customer.interests.all()]

        self.assertNotIn('reading', customer_interests)
        self.assertIn('traveling', customer_interests)
        self.assertIn('investing', customer_interests)

    # def test_redirects_after_POST(self):
    #     # Customer creation in order to fill interests
    #     default_client, _ = Customer.objects.get_or_create(name="Alberto", surname="Garcia")
    #
    #     response = self.client.post('/',
    #         {'reading': False,
    #         'investing': True,
    #         'traveling': True})
    #
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response.url, '/user/'+str(default_client.id)+'/interests')
