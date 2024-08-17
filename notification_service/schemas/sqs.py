from typing import Any

from pydantic import BaseModel

from notification_service.templates.sms import SMSTemplate


class SQSMessageSchema(BaseModel):
    destination: str
    provider: str = 'sns'
    template: SMSTemplate
    values: dict[str, Any]
