from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Pin

class PinAPITest(TestCase):
    
    def setUp(self):
        # Create a test client and a test user
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        
        # Create a sample pin in the database
        self.pin = Pin.objects.create(title="Test Pin", description="A test pin", user=self.user)
    
    def test_get_pins(self):
        # Hit the "get all pins" API endpoint
        response = self.client.get(reverse('pins'))  # Assuming 'pins' is the URL name
        # Ensure the response is HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_nonexistent_pin(self):
        # Try to get a pin that doesn’t exist (ID 999 doesn't exist)
        response = self.client.get(reverse('pin-detail', args=[999]))  # Assuming 'pin-detail' is the URL name
        # Ensure the response is HTTP 404 Not Found
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
