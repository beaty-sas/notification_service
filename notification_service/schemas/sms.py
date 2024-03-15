from typing import Any

from pydantic import BaseModel

from notification_service.templates.sms import SMSTemplate


class SMSPayloadSchema(BaseModel):
    phone_number: str
    template: SMSTemplate
    values: dict[str, Any]
