import calendar
from unittest.mock import patch

from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase, override_settings

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from api.providers.number_facts import NumberFactProvider
from fun_facts.models import FunFact


class FunFactViewSetTests(TestCase):
    fixtures = [
        'fixtures/fun_facts.json'
    ]

    def setUp(self) -> None:
        self.client = APIClient()

    def test_list(self) -> None:
        response = self.client.get(reverse('api:date-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), FunFact.objects.count())

    def test_retrieve(self) -> None:
        response = self.client.get(reverse('api:date-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    @patch.object(NumberFactProvider, 'get_fact')
    def test_create(self, mock) -> None:
        fun_facts = FunFact.objects.all()
        objects_count = fun_facts.count()
        fun_fact = 'Mocked Fact'
        mock.return_value = fun_fact
        month = 2
        day = 4
        data = {
            'month': month,
            'day': day
        }
        with self.assertRaises(ObjectDoesNotExist):
            FunFact.objects.get(month=month, day=day)
        response = self.client.post(reverse('api:date-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(fun_facts.count(), objects_count + 1)
        self.assertEqual(response.data['month'], calendar.month_name[month])
        self.assertEqual(response.data['day'], day)
        self.assertEqual(response.data['fact'], fun_fact)

    @patch.object(NumberFactProvider, 'get_fact')
    def test_create_update_existing_date_fact(self, mock) -> None:
        fun_facts = FunFact.objects.all()
        objects_count = fun_facts.count()
        fact = fun_facts.first()
        new_fun_fact = 'Mocked Fact'
        mock.return_value = new_fun_fact
        month = fact.month
        day = fact.day
        data = {
            'month': month,
            'day': day
        }
        self.assertNotEqual(fact.fact, new_fun_fact)
        response = self.client.post(reverse('api:date-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(fun_facts.count(), objects_count)
        self.assertEqual(response.data['month'], calendar.month_name[month])
        self.assertEqual(response.data['day'], day)
        self.assertEqual(response.data['fact'], new_fun_fact)

    def test_update(self) -> None:
        response = self.client.put(reverse('api:date-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_partial_update(self) -> None:
        response = self.client.patch(reverse('api:date-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete(self) -> None:
        secret_key = 'ad7g653vtfds'
        headers = {'HTTP_X_API_KEY': secret_key}
        with override_settings(SECRET_KEY=secret_key):
            response = self.client.delete(reverse('api:date-detail', args=[1]), **headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_failed_permission(self) -> None:
        secret_key = 'ad7g653vtfds'
        incorrect_secret_key = 'ad7g653vtfds1111'
        headers = {'HTTP_X_API_KEY': incorrect_secret_key}
        with override_settings(SECRET_KEY=secret_key):
            response = self.client.delete(reverse('api:date-detail', args=[1]), **headers)
            self.assertNotEqual(secret_key, incorrect_secret_key)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
