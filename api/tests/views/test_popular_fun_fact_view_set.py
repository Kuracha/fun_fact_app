import calendar

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from fun_facts.models import FunFact


class PopularFunFactViewSetTests(TestCase):
    fixtures = [
        'fixtures/fun_facts.json'
    ]

    def setUp(self) -> None:
        self.client = APIClient()

    def test_list(self) -> None:
        fun_facts = FunFact.objects.all()
        months = fun_facts.values_list('month', flat=True).distinct()
        response = self.client.get(reverse('api:popular-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for month in months:
            month_name = calendar.month_name[month]
            month_facts_count = fun_facts.filter(month=month).count()
            for fact in response.data:
                if fact.get('month') == month_name:
                    self.assertEqual(fact.get('days_checked'), month_facts_count)
                    break
            else:
                self.fail(f'Test failed because there is no data for month: {month_name} in response data')

    def test_update(self) -> None:
        response = self.client.put(reverse('api:popular-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_partial_update(self) -> None:
        response = self.client.patch(reverse('api:popular-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_retrieve(self) -> None:
        response = self.client.get(reverse('api:popular-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete(self) -> None:
        response = self.client.delete(reverse('api:popular-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_create(self) -> None:
        response = self.client.post(reverse('api:popular-list'), data={})
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
