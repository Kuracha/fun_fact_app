import traceback
from typing import Optional
from rest_framework.response import Response
import requests
import logging

from django.conf import settings

logger = logging.getLogger(settings.FILE_LOGGER_NAME)


class NumberFactProvider:
    BASE_URL = f'http://numbersapi.com/'

    def get_fact(self, month: int, day: int) -> Optional[str]:
        number = f'{month}/{day}'
        url = f'{self.BASE_URL}{number}/date'
        try:
            response = self._call_request(url)
            if response.status_code == 200:
                return response.content.decode('utf-8')
            else:
                logger.error(f"API request [{url}] failed with status code: {response.status_code}")
        except Exception as e:
            logger.error(f"Connection to the API [{url}] failed with error: {traceback.format_exc()}")
        return None

    @staticmethod
    def _call_request(url: str) -> Response:
        return requests.get(url)
