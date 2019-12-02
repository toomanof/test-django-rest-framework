import json
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from .models import Application
from .serializers import ApplicationSerializer


client = Client()

class ApplicationTest(TestCase):

    def setUp(self):
        Application.objects.create(title='test app 1')
        Application.objects.create(title='test app 2')
        Application.objects.create(title='test app 3')
        Application.objects.create(title='test app 4')

    def test_all_application(self):
        print('Тест вывод списка приложений')
        response = client.get(reverse('app_list'))
        applications = Application.objects.all()
        serializer = ApplicationSerializer(applications, many=True)
        self.assertEqual(response.data['application'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_app_info(self):
        print('Тест вывода информации об оном приложении')
        application = Application.objects.get(title='test app 1')
        serializer = ApplicationSerializer(application)
        response = client.get(
            reverse('api_test', kwargs={'api_key': application.access_token}))
        self.assertEqual(response.data['result'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_generated_valid(self):
        print('Тест генерации API ключа c передачей правильного старого ключа')
        application = Application.objects.get(title='test app 1')
        response = client.post(
            reverse('create_token'),
            data={'api_key': application.access_token})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_generated_invalid(self):
        print('Тест генерации API ключа c передачей не правильного старого ключа')
        response = client.post(
            reverse('create_token'),
            data={'api_key': '7d964c5d-95be-4e0c-82a6-ea8cd00ffdcb'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
