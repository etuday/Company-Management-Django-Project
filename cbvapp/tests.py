from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Company

class CompanyModelTest(TestCase):
    def test_string_representation(self):
        company = Company(name="TestCo")
        self.assertEqual(str(company), company.name)
