import traceback
from typing import Optional

import requests
import logging

from django.conf import settings

logger = logging.getLogger(settings.FILE_LOGGER_NAME)


class NumberFactProvider:

    @staticmethod
    def get_fact(month: int, day: int) -> Optional[str]:
        number = f'{month}/{day}'
        url = f'http://numbersapi.com/{number}/date'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.content.decode('utf-8')
            else:
                logger.error(f"API request [{url}] failed with status code: {response.status_code}")
        except Exception as e:
            logger.error(f"Connection to the API [{url}] failed with error: {traceback.format_exc()}")
        return None
