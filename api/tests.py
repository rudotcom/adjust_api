from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class DatasetTest(APITestCase):

    def test_view_data(self):
        url = reverse('data')
        # EX: ?show=impressions,clicks&date_to=2017-06-01&group_by=channel,country&order_by=-clicks&format=json
        response = self.client.get(url, format='json', show='impressions,clicks', date_to='2017-06-01',
                                   group_by='channel,country', order_by='-clicks')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
