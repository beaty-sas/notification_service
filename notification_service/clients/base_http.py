import json
import logging
from http import HTTPStatus
from typing import Type
from urllib.parse import urljoin

import httpx
from httpx import Response

from notification_service.conf.settings import settings
from notification_service.exception import HTTPClientException

logger = logging.getLogger(__name__)


class BaseHTTPClient:
    EXC_CLASS: Type[HTTPClientException] = HTTPClientException
    BASE_URL: str

    def __init__(self, base_url: str | None = None, timeout: float = settings.BASE_HTTP_CLIENT_TIMEOUT):
        self.base_url = base_url or self.BASE_URL
        self.timeout = timeout

    def _request(self, url: str, method: str, **kwargs) -> Response:
        full_path = self.get_url(url)
        self._before_request_log(method, url, **kwargs)
        try:
            response = httpx.request(method=method, url=full_path, timeout=self.timeout, **kwargs)
        except Exception as err:
            raise self.EXC_CLASS(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                response_text=str(err),
                url=full_path,
            )
        self._after_response_log(url=url, response=response)
        self._check_response(response)
        return response

    def get_url(self, url: str) -> str:
        return urljoin(self.base_url, url)  # type: ignore

    def get(self, url: str, **kwargs) -> Response:
        return self._request(url, 'GET', **kwargs)

    def post(self, url: str, **kwargs) -> Response:
        return self._request(url, 'POST', **kwargs)

    def patch(self, url: str, **kwargs) -> Response:
        return self._request(url, 'PATCH', **kwargs)

    def _check_response(self, response: httpx.Response) -> None:
        if response.is_error:
            raise self.EXC_CLASS(
                status_code=response.status_code,
                response_text=response.text,
                url=str(response.url),
            )

    @staticmethod
    def _before_request_log(url: str, method: str, **kwargs) -> None:
        """Log message before request started"""
        data = kwargs.get('json') or kwargs.get('data') or kwargs.get('params') or {}
        if isinstance(data, dict):
            data = json.dumps(data)

        logger.info(
            {
                'message': f'External {method} request to {url}',
                'text': data,
            }
        )

    @staticmethod
    def _after_response_log(url: str, response: httpx.Response) -> None:
        """Log message ofter receiving response"""
        logger.info(
            {
                'message': f'Received response from {url} with status code {response.status_code}',
                'text': response.text,
            }
        )
