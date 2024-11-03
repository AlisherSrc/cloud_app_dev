from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

class UserIntegrationTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')
        self.login_url = reverse('login')

    def test_user_registration(self):
        user_data = {
            'username': 'integrationuser',
            'password': 'testpassword',
            'email': 'integrationuser@example.com'
        }
        response = self.client.post(self.register_url, user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='integrationuser').exists())

    def test_user_authentication(self):
        # First, create a user
        User.objects.create_user(username='integrationuser', password='testpassword')
        login_data = {
            'username': 'integrationuser',
            'password': 'testpassword'
        }
        response = self.client.post(self.login_url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)