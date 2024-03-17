import time

import httpx

from notification_service.clients.base_http import BaseHTTPClient
from notification_service.conf.settings import settings
from notification_service.templates.sms import BSGRequestData


class BSGProvider(BaseHTTPClient):
    """Documentation: https://bsg.world/documentations/rest-api/sms-api/sending-sms/"""

    BASE_URL = settings.BSG_URL

    class ROUTES:
        SEND_SMS: str = '/rest/sms/create'

    @property
    def headers(self):
        return {'X-API-KEY': settings.BSG_API_KEY}

    def send_sms(self, destination: str, message: str) -> dict:
        data = BSGRequestData(  # type: ignore
            reference=str(int(time.time())),
            msisdn=destination,
            originator=settings.BSG_SENDER_NAME,
            body=message,
        )
        response = self.post(
            self.ROUTES.SEND_SMS,
            json=data.dict(by_alias=True, exclude_none=True),
            headers=self.headers,
        )
        return response.json()

    def _check_response(self, response: httpx.Response) -> None:
        super()._check_response(response)
        if response.json().get('result') is None:
            raise self.EXC_CLASS(
                status_code=response.status_code,
                response_text=response.text,
                url=str(response.url),
            )

        if response.json()['result'].get('error'):
            raise self.EXC_CLASS(
                status_code=response.status_code,
                response_text=response.text,
                url=str(response.url),
            )
