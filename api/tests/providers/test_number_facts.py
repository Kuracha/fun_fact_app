# Standard Library
from typing import Optional
from unittest.mock import patch

# Django
from django.http import HttpResponse
from django.test import TestCase

# 3rd-party
import requests
from rest_framework import status

# Project
from api.providers.number_facts import NumberFactProvider


class NumberFactProviderTests(TestCase):
    fixtures = [
        'fixtures/fun_facts.json'
    ]

    @patch.object(NumberFactProvider, '_call_request')
    def test_get_fact_success(self, mock) -> None:
        fact = 'This is some fact.'
        response_data = HttpResponse(fact, content_type="text/plain")
        mock.return_value = response_data
        response = self._get_test_response()
        self.assertEqual(response, fact)

    @patch.object(NumberFactProvider, '_call_request')
    def test_get_fact_fail(self, mock) -> None:
        fact = 'This is some fact.'
        response_data = HttpResponse(fact, content_type="text/plain", status=status.HTTP_400_BAD_REQUEST)
        mock.return_value = response_data
        response = self._get_test_response()
        self.assertEqual(response, None)

    @patch.object(NumberFactProvider, '_call_request')
    def test_get_fact_exception(self, mock) -> None:
        mock.side_effect = requests.ConnectionError
        response = self._get_test_response()
        self.assertEqual(response, None)

    def _get_test_response(self) -> Optional[str]:
        month = 1
        day = 1
        return NumberFactProvider().get_fact(month, day)
