from django.test import TestCase

# Create your tests here.
class MathFailingTest(TestCase):

    def test_bad_math(self):
        self.assertEqual(1 + 1, 3, '1 + 1 is not 3')
