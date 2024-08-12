from typing import Any

from notification_service.clients.sns import AWSSNSClient
from notification_service.templates.sms import SMSTemplate


class SMSNotification:
    NAME: SMSTemplate
    VALUES: dict[str, list[str]]
    TEMPLATE: str

    def __init__(self, values: dict[str, Any]):
        self.values = values
        self.provider = AWSSNSClient()

    def process_sms(self, destination: str) -> None:
        message = self.TEMPLATE.format(**self.values)
        self.provider.send_sms(destination, message)
