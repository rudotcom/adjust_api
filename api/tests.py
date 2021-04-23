from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import SampleDataSet


class DatasetTest(APITestCase):

    def test_view_data(self):

        url = reverse('data')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
