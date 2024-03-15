from typing import Any

import ujson


class HTTPClientException(Exception):
    def __init__(self, url: str, status_code: int, response_text: str):
        self.url = url
        self.status_code = status_code
        self.response_text = response_text

    def json(self) -> dict[str, Any]:
        try:
            return ujson.loads(self.response_text)

        except ValueError:
            return {}

    def __str__(self) -> str:
        return f'URL {self.url} responded with {self.status_code}. RESPONSE: {self.response_text}'

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} status_code={self.status_code}>'
