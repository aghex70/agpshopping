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

        user_selected_interests = {'personal_interests': [str(investing_interest.id),
         str(traveling_interest.id)]}
        response = self.client.post('/',
        data=user_selected_interests)

        new_customer = Customer.objects.get(name="John", surname="Doe")
        customer_interests = [category.name for category in new_customer.interests.all()]

        self.assertNotIn('reading', customer_interests)
        self.assertIn('traveling', customer_interests)
        self.assertIn('investing', customer_interests)

    def test_can_save_an_empty_POST_request(self):
        Customer.objects.get_or_create(name="John", surname="Doe")

        user_selected_interests = {}
        response = self.client.post('/', data=user_selected_interests)

        new_customer = Customer.objects.get(name="John", surname="Doe")
        customer_interests = [category.name for category in new_customer.interests.all()]

        self.assertNotIn('reading', customer_interests)
        self.assertNotIn('traveling', customer_interests)
        self.assertNotIn('investing', customer_interests)

    def test_redirects_after_POST(self):
        default_client, _ = Customer.objects.get_or_create(name="John", surname="Doe")

        response = self.client.post('/', {})

        self.assertRedirects(response, '/user/'+str(default_client.id)+'/interests/')
        # self.assertEqual(response.status_code, 302)
        # self.assertEqual(response.url, '/user/'+str(default_client.id)+'/interests')

class ListViewTest(TestCase):
    def test_uses_list_template(self):
        new_customer, _ = Customer.objects.get_or_create(name="John", surname="Doe")
        another_new_customer, _ = Customer.objects.get_or_create(name="Jane", surname="Doe")
        response = self.client.get(f'/user/{another_new_customer.id}/interests/')
        self.assertTemplateUsed(response, 'user_interests_list.html')
