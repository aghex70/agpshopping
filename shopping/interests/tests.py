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
        # Customer creation in order to fill interests
        Customer.objects.get_or_create(name="Alberto", surname="Garcia")

        post_data = {'reading': False,
            'investing': True,
            'traveling': True}


        form = InterestsForm(data=post_data)

        response = self.client.post('/',
        post_data)

        print(response.content)

        new_customer = Customer.objects.first()

        customer_interests = [category.name for category in new_customer.interests.all()]
        for i in customer_interests:
            print(i)
        print("FIN")

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
